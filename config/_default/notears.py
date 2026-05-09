#%%
import torch
import numpy as np
import scipy.linalg as slin
from scipy.special import expit as sigmoid
from notears import utils  # Assuming you have the notears utils module


def notears_linear(X, lambda1, loss_type, max_iter=100, h_tol=1e-8, rho_max=1e+16, w_threshold=0.3):
    def _loss(W, M):
        if loss_type == 'l2':
            R = X - M
            loss = 0.5 / X.shape[0] * (R ** 2).sum()
            G_loss = - 1.0 / X.shape[0] * X.T @ R
        elif loss_type == 'logistic':
            loss = 1.0 / X.shape[0] * (torch.log(1 + torch.exp(M)) - X * M).sum()
            G_loss = 1.0 / X.shape[0] * X.T @ (sigmoid(M) - X)
        elif loss_type == 'poisson':
            S = torch.exp(M)
            loss = 1.0 / X.shape[0] * (S - X * M).sum()
            G_loss = 1.0 / X.shape[0] * X.T @ (S - X)
        else:
            raise ValueError('unknown loss type')
        return loss

    def _h(W):
        E = slin.expm((W * W).cpu().detach().numpy())  # convert to numpy for matrix exponential
        h = np.trace(E) - d
        G_h = torch.tensor(E.T * W.cpu().detach().numpy() * 2)  # convert back to tensor
        return h, G_h

    n, d = X.shape
    X = torch.tensor(X, requires_grad=False, dtype=torch.float32)
    W = torch.zeros((d, d), requires_grad=True)

    # Optimizer
    optimizer = torch.optim.Adam([W], lr=1e-3)

    rho, alpha = 1.0, 0.0
    for _ in range(max_iter):
        optimizer.zero_grad()

        M = X @ W
        loss = _loss(W, M)
        h, G_h = _h(W)
        augmented_lagrangian = loss + 0.5 * rho * h * h + alpha * h + lambda1 * W.abs().sum()
        augmented_lagrangian.backward()
        optimizer.step()

        h, _ = _h(W)
        alpha += rho * h

        if h <= h_tol or rho >= rho_max:
            break

    W_est = W.detach().numpy()
    W_est[np.abs(W_est) < w_threshold] = 0
    return W_est


if __name__ == '__main__':
    utils.set_random_seed(1)

    n, d, s0, graph_type, sem_type = 100, 20, 20, 'ER', 'gauss'
    B_true = utils.simulate_dag(d, s0, graph_type)
    W_true = utils.simulate_parameter(B_true)
    np.savetxt('W_true.csv', W_true, delimiter=',')

    X = utils.simulate_linear_sem(W_true, n, sem_type)
    np.savetxt('X.csv', X, delimiter=',')

    W_est = notears_linear(X, lambda1=0.1, loss_type='l2')
    assert utils.is_dag(W_est)
    np.savetxt('W_est.csv', W_est, delimiter=',')
    acc = utils.count_accuracy(B_true, W_est != 0)
    print(acc)
