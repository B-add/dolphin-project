import numpy as np
from cvxopt import matrix, solvers

def approx_weight(cov, R, q, l=0.01, h=0.1):
    Q_ = (cov + 2 - 2 * np.eye(R.shape[0])) / 2 + (cov * np.eye(R.shape[0])) / 2
    Q = matrix(Q_)

    p = matrix(-q * R)

    a1 = -np.eye(cov.shape[0])
    b1 =  np.eye(cov.shape[0])

    G = matrix(np.concatenate((a1, b1), axis=0))

    h = matrix([l] * cov.shape[0] + [h] * cov.shape[0])
    A = matrix([[1.0] * cov.shape[0]], (1,cov.shape[0]))
    b = matrix(1.0)

    sol = solvers.qp(Q, p, G, h, A, b)

    w_op = np.array(sol['x'])
    w_op = w_op.reshape((cov.shape[0],))

    return w_op
