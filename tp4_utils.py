import numpy as np
import matplotlib.pyplot as plt


def verifier(nom, valeur, attendu, tol=1e-3):
    ok = np.allclose(valeur, attendu, atol=tol, rtol=tol)
    print(("✅" if ok else "❌") + f" {nom}")
    if not ok:
        print("  obtenu :", valeur)
        print("  attendu:", attendu)
    return ok


def tracer_groupes(X, etiquettes, centres=None, ax=None, titre="", axes=("x1", "x2")):
    if ax is None:
        _, ax = plt.subplots()
    for groupe in np.unique(etiquettes):
        ax.scatter(X[etiquettes == groupe, 0], X[etiquettes == groupe, 1],
                   label=f"cluster {groupe}")
    if centres is not None:
        ax.scatter(centres[:, 0], centres[:, 1], marker="X", c="black",
                   s=100, label="centroïdes")
    ax.set_xlabel(axes[0])
    ax.set_ylabel(axes[1])
    ax.set_title(titre)
    ax.legend()
    return ax
