#!/bin/bash
hugo && rsync -avz --delete public/ hyan46@general.asu.
