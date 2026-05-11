import marimo

__generated_with = "0.20.4"
app = marimo.App()


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    # Redstart: A Lightweight Reusable Booster
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.image(src="public/images/redstart.png")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Project Redstart is an attempt to design the control systems of a reusable booster during landing.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    In principle, it is similar to SpaceX's Falcon Heavy Booster.

    >The Falcon Heavy booster is the first stage of SpaceX's powerful Falcon Heavy rocket, which consists of three modified Falcon 9 boosters strapped together. These boosters provide the massive thrust needed to lift heavy payloads—like satellites or spacecraft—into orbit. After launch, the two side boosters separate and land back on Earth for reuse, while the center booster either lands on a droneship or is discarded in high-energy missions.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.center(
        mo.Html("""
    <iframe width="560" height="315" src="https://www.youtube.com/embed/RYUr-5PYA7s?si=EXPnjNVnqmJSsIjc" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>""")
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Dependencies
    """)
    return


@app.cell
def _():
    import scipy
    import scipy.integrate as sci

    import matplotlib as mpl
    import matplotlib.pyplot as plt

    import numpy as np
    import numpy.linalg as la

    return np, plt, sci


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## The Model

    The Redstart booster in model as a rigid tube of length $\ell$ and negligible diameter whose mass $M$ is uniformly spread along its length. It may be located in 2D space by the coordinates $(x, y)$ of its center of mass and the angle $\theta$ it makes with respect to the vertical (with the convention that $\theta > 0$ for a left tilt, i.e. the angle is measured counterclockwise)

    This booster has an orientable reactor at its base ; the force that it generates is of amplitude $f \geq 0$ and the angle of the force with respect to the booster axis is $\phi$ (with a counterclockwise convention).

    We assume that the booster is subject to gravity, the reactor force and that the friction of the air is negligible.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.center(mo.image(src="public/images/geometry.svg"))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Constants

    For the sake of simplicity (this is merely a toy model!) in the sequel we assume that:

    - the total length $\ell$ of the booster is 2 meters,
    - its mass $M$ is 1 kg,
    - the gravity constant $g$ is 1 m/s^2.

    This set of values is completely unrealistic, but very simple! It will simplify our computations and will not fundamentally impact the structure of the booster dynamics.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Getting Started
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Constants

    Define the Python constants `g`, `M` and `l` that correspond to the gravity constant, the mass and half-length of the booster.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    D'après l'énoncé on a :

    \[
    \ell = 2 \ \text{m}
    \]

    La masse du booster est :

    \[
    M = 1 \ \text{kg}
    \]

    et la constante gravitationnelle est :

    \[
    g = 1 \ \text{m/s}^2
    \]
    """)
    return


@app.cell
def _():
    l = 2
    M = 1
    g = 1
    return M, g, l


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Forces

    Compute the cartesian coordinates $f_x$ and $f_y$ of the force applied to the booster by the reactor, functions of $f$, $\theta$ and $\phi$.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    On considère une force $\vec f$ de norme $f$ exprimée dans le repère
    $(x',y')$ :

    $$
    \vec f
    =
    f\cos(\phi)\,\vec e_{y'}
    -
    f\sin(\phi)\,\vec e_{x'}
    $$

    où :

    - $f = \|\vec f\|$ est la norme de la force,
    - $\vec e_{x'}$ et $\vec e_{y'}$ sont les vecteurs de base du repère $(x',y')$,
    - $\phi$ représente l’angle de la force dans ce repère.

    ---

    On souhaite exprimer cette même force dans le repère
    $(x,y)$ de base $(\vec e_x,\vec e_y)$.

    Les deux repères sont liés par une rotation d’angle $\theta$.

    Les relations de changement de base sont :

    $$
    \vec e_{y'}
    =
    \cos(\theta)\,\vec e_y
    -
    \sin(\theta)\,\vec e_x
    $$

    $$
    \vec e_{x'}
    =
    \sin(\theta)\,\vec e_y
    +
    \cos(\theta)\,\vec e_x
    $$

    ---

    On remplace alors $\vec e_{x'}$ et $\vec e_{y'}$
    dans l’expression de $\vec f$ :

    $$
    \vec f
    =
    f\cos(\phi)
    \left(
    \cos(\theta)\,\vec e_y
    -
    \sin(\theta)\,\vec e_x
    \right)
    -
    f\sin(\phi)
    \left(
    \sin(\theta)\,\vec e_y
    +
    \cos(\theta)\,\vec e_x
    \right)
    $$

    En développant :

    $$
    \vec f
    =
    f\cos(\phi)\cos(\theta)\,\vec e_y
    -
    f\cos(\phi)\sin(\theta)\,\vec e_x
    -
    f\sin(\phi)\sin(\theta)\,\vec e_y
    -
    f\sin(\phi)\cos(\theta)\,\vec e_x
    $$

    On regroupe les termes selon les vecteurs de base :

    $$
    \vec f
    =
    f\left(
    \cos(\phi)\cos(\theta)
    -
    \sin(\phi)\sin(\theta)
    \right)\vec e_y
    -
    f\left(
    \cos(\phi)\sin(\theta)
    +
    \sin(\phi)\cos(\theta)
    \right)\vec e_x
    $$

    En utilisant les identités trigonométriques :

    $$
    \cos(a+b)
    =
    \cos a \cos b - \sin a \sin b
    $$

    $$
    \sin(a+b)
    =
    \sin a \cos b + \cos a \sin b
    $$

    on obtient finalement :

    $$
    \boxed{
    \vec f
    =
    f\cos(\phi+\theta)\,\vec e_y
    -
    f\sin(\phi+\theta)\,\vec e_x
    }
    $$

    Cette expression représente la force $\vec f$
    dans le repère $(x,y)$.
    """)
    return


@app.cell
def _(np):
    def force_components(f, theta, phi):
        fx = -f * np.sin(theta + phi)
        fy = f * np.cos(theta + phi)
        return fx, fy

    return (force_components,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Center of Mass

    Give the ordinary differential equation that governs the evolution of the position $(x, y)$ of the center of mass of the booster.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Center of Mass

    On cherche l’équation différentielle qui gouverne l’évolution de la position du centre de masse du booster :

    $$
    (x(t),y(t)).
    $$

    Le booster est soumis à deux actions mécaniques extérieures principales :

    1. la force de poussée du réacteur :

    $$
    \vec{F}
    =
    \begin{bmatrix}
    f_x \\
    f_y
    \end{bmatrix}
    $$

    2. le poids du booster :

    $$
    \vec{P}
    =
    \begin{bmatrix}
    0 \\
    -Mg
    \end{bmatrix}.
    $$

    ---

    D’après le principe fondamental de la dynamique appliqué au centre de masse :

    $$
    M\vec{a}_G = \sum \vec{F}_{ext}
    $$

    où :

    $$
    \vec{a}_G
    =
    \begin{bmatrix}
    \ddot{x} \\
    \ddot{y}
    \end{bmatrix}
    $$

    est l’accélération du centre de masse.

    Donc :

    $$
    M
    \begin{bmatrix}
    \ddot{x} \\
    \ddot{y}
    \end{bmatrix}
    =
    \begin{bmatrix}
    f_x \\
    f_y
    \end{bmatrix}
    +
    \begin{bmatrix}
    0 \\
    -Mg
    \end{bmatrix}.
    $$

    Ainsi :

    $$
    M
    \begin{bmatrix}
    \ddot{x} \\
    \ddot{y}
    \end{bmatrix}
    =
    \begin{bmatrix}
    f_x \\
    f_y - Mg
    \end{bmatrix}.
    $$

    ---

    On en déduit les deux équations scalaires :

    $$
    M\ddot{x}=f_x
    $$

    et :

    $$
    M\ddot{y}=f_y-Mg.
    $$

    Donc :

    $$
    \ddot{x}=\frac{f_x}{M}
    $$

    et :

    $$
    \ddot{y}=\frac{f_y}{M}-g.
    $$

    ---

    D’après la question précédente, les composantes de la force de poussée sont :

    $$
    f_x=-f\sin(\theta+\phi)
    $$

    et :

    $$
    f_y=f\cos(\theta+\phi).
    $$

    En remplaçant dans les équations du mouvement, on obtient :

    $$
    \ddot{x}
    =
    -\frac{f}{M}\sin(\theta+\phi)
    $$

    et :

    $$
    \ddot{y}
    =
    \frac{f}{M}\cos(\theta+\phi)-g.
    $$

    ---

    Finalement,

    $$
    \boxed{
    \begin{bmatrix}
    \ddot{x} \\
    \ddot{y}
    \end{bmatrix}
    =
    \begin{bmatrix}
    -\dfrac{f}{M}\sin(\theta+\phi) \\
    \dfrac{f}{M}\cos(\theta+\phi)-g
    \end{bmatrix}
    }
    $$

    Cette équation décrit la dynamique de translation du booster. Elle montre que la poussée contrôle simultanément le mouvement horizontal et vertical, tandis que la gravité agit uniquement sur l’axe vertical.
    """)
    return


@app.cell
def _(M, force_components, g):
    def center_of_mass_acceleration(f, theta, phi):
        fx, fy = force_components(f, theta, phi)

        x_ddot = fx / M
        y_ddot = (fy / M) - g

        return x_ddot, y_ddot

    return (center_of_mass_acceleration,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Moment of inertia

    Compute the [moment of inertia](https://en.wikipedia.org/wiki/Moment_of_inertia) $J$ of the booster and define the corresponding Python variable `J`.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Le booster est assimilé à une barre homogène de masse \(M\) et de longueur totale \(\ell\).

    Le moment d’inertie d’une barre autour de son centre est donné par :

    \[
    J = \frac{1}{12} M \ell^2
    \]

    D’après l’énoncé :

    \[
    \ell = 2 \ \text{m}, \quad M = 1 \ \text{kg}
    \]

    Donc :

    \[
    J = \frac{1}{12} \times 1 \times 2^2
    \]

    \[
    J = \frac{1}{12} \times 4 = \frac{1}{3}
    \]

    Ainsi :

    \[
    \boxed{
    J = \frac{1}{3} \ \text{kg}\cdot\text{m}^2
    }
    \]
    """)
    return


@app.cell
def _(M, l):
    J = (1.0 / 12.0) * M * l**2
    J
    return (J,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Tilt

    Give the ordinary differential equation that governs the evolution of the tilt angle $\theta$.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    La force est appliquée à la base du booster.

    La composante perpendiculaire de la force vaut :

    $$
    f\sin(\phi)
    $$

    Le couple algébrique est donc :

    $$
    \tau=-\frac{l}{2}f\sin(\phi)
    $$

    Avec :

    $$
    J\ddot{\theta}=\tau
    $$

    on obtient :

    $$
    J\ddot{\theta}=-\frac{l}{2}f\sin(\phi)
    $$

    Donc :

    $$
    \boxed{
    \ddot{\theta}=-\frac{lf}{2J}\sin(\phi)
    }
    $$
    """)
    return


@app.cell
def _(J, l, np):
    def tilt_acceleration(f, phi):
        theta_ddot = -(l * f / (2 * J)) * np.sin(phi)
        return theta_ddot

    return (tilt_acceleration,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Vector Field

    Denote

    - $v_x =\dot{x}$, $v_y = \dot{y}$ the components of the booster center of mass velocity,
    - $\omega = \dot{\theta}$ the angular velocity of the booster.


    What is is dimension $n$ of the state space?
    What is the state $s \in \R^n$ of the booster dynamics?
    Provide the definition of the function $F : \mathbb{R}^{n + 2} \to \mathbb{R}^n$ such that the system evolves
    according to

    $$
    \dot{s} = F(s, f, \phi).
    $$
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    On définit l’état du système par :

    $$
    s =
    \begin{bmatrix}
    x \\
    v_x \\
    y \\
    v_y \\
    \theta \\
    \omega
    \end{bmatrix}
    $$

    avec :

    $$
    v_x=\dot{x},
    \qquad
    v_y=\dot{y},
    \qquad
    \omega=\dot{\theta}.
    $$

    La dimension de l’espace d’état est donc :

    $$
    \boxed{n=6}
    $$

    Les équations du mouvement sont :

    $$
    \ddot{x}
    =
    -\frac{f}{M}\sin(\theta+\phi)
    $$

    $$
    \ddot{y}
    =
    \frac{f}{M}\cos(\theta+\phi)-g
    $$

    $$
    \ddot{\theta}
    =
    -\frac{lf}{2J}\sin(\phi)
    $$

    Donc le système sous forme d’état est :

    $$
    \dot{s}
    =
    F(s,f,\phi)
    $$

    avec :

    $$
    F(s,f,\phi)
    =
    \begin{bmatrix}
    v_x \\
    -\dfrac{f}{M}\sin(\theta+\phi) \\
    v_y \\
    \dfrac{f}{M}\cos(\theta+\phi)-g \\
    \omega \\
    -\dfrac{lf}{2J}\sin(\phi)
    \end{bmatrix}.
    $$

    Ainsi :

    $$
    \boxed{
    F(s,f,\phi)
    =
    \begin{bmatrix}
    v_x \\
    -\dfrac{f}{M}\sin(\theta+\phi) \\
    v_y \\
    \dfrac{f}{M}\cos(\theta+\phi)-g \\
    \omega \\
    -\dfrac{lf}{2J}\sin(\phi)
    \end{bmatrix}
    }
    $$
    """)
    return


@app.cell
def _(center_of_mass_acceleration, np, tilt_acceleration):
    def F(s, f, phi):
        x, vx, y, vy, theta, omega = s

        x_dot = vx
        y_dot = vy
        theta_dot = omega

        vx_dot, vy_dot = center_of_mass_acceleration(f, theta, phi)
        omega_dot = tilt_acceleration(f, phi)

        return np.array([
            x_dot,
            vx_dot,
            y_dot,
            vy_dot,
            theta_dot,
            omega_dot,
        ])

    return (F,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Simulation

    Define a function `redstart_solve` that, given the input parameters:

    - `t_span`: a pair of initial time `t_0` and final time `t_f`,
    - `y0`: the value of `[x, vx, y, vy, theta, omega]` at `t_0`,
    - `f_phi`: a function that given the current time `t` and current state value `y`
         returns the values of the inputs `f` and `phi` in an array.

    returns:

    - `sol`: a function that given a time `t` returns the value of `[x, vx, y, vy, theta, omega]` at time `t` (and that also accepts 1d-arrays of times for multiple state evaluations).

    A typical usage would be:

    ```python
    def free_fall_example():
        t_span = [0.0, 5.0]
        y0 = [0.0, 0.0, 10.0, 0.0, 0.0, 0.0] # [x, vx, y, vy, theta, omega]
        def f_phi(t, y):
            return np.array([0.0, 0.0]) # [f, phi]
        sol = redstart_solve(t_span, y0, f_phi)
        t = np.linspace(t_span[0], t_span[1], 1000)
        y_t = sol(t)[2]
        plt.plot(t, y_t, label=r"$y(t)$ (height in meters)")
        plt.plot(t, l * np.ones_like(t), color="grey", ls="--", label=r"$y=\ell$")
        plt.title("Free Fall")
        plt.xlabel("time $t$")
        plt.grid(True)
        plt.legend()
        return plt.gcf()
    free_fall_example()
    ```
    """)
    return


@app.cell
def _(F, sci):
    def redstart_solve(t_span, y0, f_phi):
        def fphi(t, y):
            f, phi = f_phi(t, y)
            return F(y, f, phi)

        sol_ivp = sci.solve_ivp(
            fphi,
            t_span,
            y0,
            dense_output=True,
            max_step=0.05
        )

        return sol_ivp.sol

    return (redstart_solve,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Freefall test


    In the `free_fall` example scenario. scenario, at what moment should the center of mass of the booster theoretically cross the
    height of $y = \ell$?

    Check your `redstart_solve` function in this scenario and produce a graph that allows us to check the above answer numerically/visually.
    """)
    return


@app.cell
def _(g, l, np, plt, redstart_solve):
    def free_fall_test():
        t_span = [0.0, 5.0]

        y0 = np.array([
            0.0,   # x
            0.0,   # vx
            10.0,  # y
            0.0,   # vy
            0.0,   # theta
            0.0,   # omega
        ])

        def f_phi(t, y):
            return np.array([0.0, 0.0])

        sol = redstart_solve(t_span, y0, f_phi)

        t = np.linspace(t_span[0], t_span[1], 1000)
        s_t = sol(t)

        y_t = s_t[2]
        t_cross = np.sqrt(2 * (10.0 - l / 2.0) / g)

        plt.figure()
        plt.plot(t, y_t, label=r"$y(t)$")
        plt.axhline(l / 2.0, color="grey", ls="--", label=r"$y=l/2$")
        plt.axvline(t_cross, color="red", ls="--", label=fr"$t \approx {t_cross:.3f}$")
        plt.xlabel("time $t$")
        plt.ylabel("height $y(t)$")
        plt.title("Free Fall")
        plt.grid(True)
        plt.legend()

        return plt.gcf()

    free_fall_test()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Controlled Landing

    Assume that $x$, $\dot{x}$, $\theta$ and $\dot{\theta}$ are null at $t=0$ and that $y(0)= 10$ and $\dot{y}(0) = - 2$.

    Find a time-varying force $f(t)$ which, when applied in the booster axis ($\theta=0$), yields $y(5)=\ell / 2 = 1$ (the booster is at ground level) and $\dot{y}(5)=0$ (the booster is at rest).

    Simulate the corresponding scenario, display graphically the results and check that your solution works as expected.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    On veut faire atterrir le booster verticalement.

    Les conditions initiales sont :

    $$
    x(0)=0,
    \qquad
    \dot{x}(0)=0,
    $$

    $$
    y(0)=10,
    \qquad
    \dot{y}(0)=-2,
    $$

    $$
    \theta(0)=0,
    \qquad
    \dot{\theta}(0)=0.
    $$

    L’objectif est d’obtenir, à l’instant $t=5$ :

    $$
    y(5)=\frac{l}{2}
    $$

    et :

    $$
    \dot{y}(5)=0.
    $$

    Comme $l=2$, cela donne :

    $$
    y(5)=1.
    $$

    On choisit une stratégie d’atterrissage vertical, donc la poussée reste alignée avec l’axe du booster :

    $$
    \phi(t)=0.
    $$

    Comme le booster est initialement vertical, on garde :

    $$
    \theta(t)=0.
    $$

    La dynamique verticale devient alors :

    $$
    \ddot{y}(t)=\frac{f(t)}{M}-g.
    $$

    On choisit une accélération verticale désirée affine en temps :

    $$
    \ddot{y}(t)=a+bt.
    $$

    En intégrant une première fois :

    $$
    \dot{y}(t)=-2+at+\frac{b}{2}t^2.
    $$

    En intégrant une deuxième fois :

    $$
    y(t)=10-2t+\frac{a}{2}t^2+\frac{b}{6}t^3.
    $$

    On impose les conditions finales :

    $$
    \dot{y}(5)=0
    $$

    et :

    $$
    y(5)=1.
    $$

    Cela donne :

    $$
    -2+5a+\frac{25}{2}b=0
    $$

    et :

    $$
    \frac{25}{2}a+\frac{125}{6}b=1.
    $$

    En résolvant ce système, on obtient :

    $$
    a=-\frac{14}{25},
    \qquad
    b=\frac{48}{125}.
    $$

    Donc :

    $$
    \ddot{y}(t)
    =
    -\frac{14}{25}
    +
    \frac{48}{125}t.
    $$

    Or :

    $$
    \ddot{y}(t)=\frac{f(t)}{M}-g.
    $$

    Ainsi :

    $$
    f(t)=M\left(\ddot{y}(t)+g\right).
    $$

    Donc la loi de poussée est :

    $$
    \boxed{
    f(t)=M\left(g-\frac{14}{25}+\frac{48}{125}t\right)
    }
    $$

    avec :

    $$
    \boxed{
    \phi(t)=0.
    }
    $$
    """)
    return


@app.cell
def _(M, g):
    def controlled_landing_force(t):
        return M * (g - 14.0 / 25.0 + (48.0 / 125.0) * t)

    return (controlled_landing_force,)


@app.cell
def _(controlled_landing_force, l, np, plt, redstart_solve):
    def controlled_landing():
        t_span = [0.0, 5.0]

        y0 = np.array([
            0.0,   # x
            0.0,   # vx
            10.0,  # y
            -2.0,  # vy
            0.0,   # theta
            0.0,   # omega
        ])

        def f_phi(t, y):
            return np.array([controlled_landing_force(t), 0.0])

        sol = redstart_solve(t_span, y0, f_phi)

        t = np.linspace(t_span[0], t_span[1], 1000)
        s_t = sol(t)

        y_t = s_t[2]
        vy_t = s_t[3]
        f_t = np.array([controlled_landing_force(ti) for ti in t])

        plt.figure()
        plt.plot(t, y_t, label=r"$y(t)$")
        plt.plot(t, vy_t, label=r"$\dot{y}(t)$")
        plt.plot(t, f_t, label=r"$f(t)$")
        plt.axhline(l / 2.0, color="grey", ls="--", label=r"$y=l/2$")
        plt.axhline(0.0, color="black", ls="--", label=r"$\dot{y}=0$")
        plt.xlabel("time $t$")
        plt.title("Controlled Landing")
        plt.grid(True)
        plt.legend()

        print("y(5) =", sol(5.0)[2])
        print("vy(5) =", sol(5.0)[3])

        return plt.gcf()

    controlled_landing()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Animations

    It's very handy to visualize the evolution of our booster "as a movie"!

    Have a look at the [animations tutorial] to understand the basics of animated SVG documents.

    [animations tutorial]: http://localhost:2718/?file=animations.py
    """)
    return


@app.cell
def _():
    from svg import svg, transform, animate_transform

    return (svg,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Environment

    Create a function `world` whose arguments are:

    - `view_box`: a view box in cartesian coordinates `[x_min, x_max, y_min, y_max]`,

    - `*objects`: (optional) list of extra svg elements (default : `[]`).

    and that returns a SVG string which

    - has the appropriate cartesian view box and frame ($y$-axis upwards),

    - depicts the sky and the ground,

    - depicts a 2 meter wide green ground target centered on $(0, 0)$,

    - displays the objects (if any) inserted on top of the world.

    Test your function with the following scenes:

    ```python
    mo.hstack(
        [
            # Display an empty world
            mo.Html(
                world([-3, 3, -2, 4])
            ),
            # Display a world with a black square on top of the landing pad
            mo.Html(
                world(
                    [-3, 3, -2, 4],
                    svg.rect(x=-1, y=0, width=2, height=2, fill="black"),
                )
            ),
            # Display a world with a red square in the top-left corner of the view box
            # and a blue square on the top-right corner of the view box.
            mo.Html(
                world(
                    [-3, 3, -2, 4],
                    svg.rect(x=-3, y=2, width=2, height=2, fill="red"),
                    svg.rect(x=1, y=2, width=2, height=2, fill="blue"),
                )
            )
        ],
        justify="space-around"
    )
    ```
    """)
    return


@app.cell
def _(np):
    def world(view_box, *objects, title=None):
        x_min, x_max, y_min, y_max = view_box
        width = x_max - x_min
        height = y_max - y_min

        def svg_y(y):
            return -y

        # Background
        sky = f'''
        <rect x="{x_min}" y="0" width="{width}" height="{y_max}" fill="#7ec8e3" />
        '''

        ground = f'''
        <rect x="{x_min}" y="{y_min}" width="{width}" height="{-y_min}" fill="#9b662b" />
        '''

        # Grid
        grid = []
        for x_tick in range(int(np.floor(x_min)), int(np.ceil(x_max)) + 1):
            grid.append(
                f'<line x1="{x_tick}" y1="{y_min}" x2="{x_tick}" y2="{y_max}" '
                f'stroke="#888" stroke-width="0.015" opacity="0.35" />'
            )

        for y_tick in range(int(np.floor(y_min)), int(np.ceil(y_max)) + 1):
            grid.append(
                f'<line x1="{x_min}" y1="{y_tick}" x2="{x_max}" y2="{y_tick}" '
                f'stroke="#888" stroke-width="0.015" opacity="0.35" />'
            )

        # Axes
        axes = [
            f'<line x1="{x_min}" y1="0" x2="{x_max}" y2="0" '
            f'stroke="black" stroke-width="0.025" opacity="0.75" />',

            f'<line x1="0" y1="{y_min}" x2="0" y2="{y_max}" '
            f'stroke="black" stroke-width="0.025" opacity="0.75" />',
        ]

        # Landing target
        target = '''
        <rect x="-1" y="0" width="2" height="0.10" fill="#0b8f20" />
        <rect x="-1" y="0.10" width="2" height="0.03" fill="#096d19" />
        '''

        # Objects are drawn in mathematical coordinates
        scene_content = "\n".join([
            sky,
            ground,
            *grid,
            *axes,
            target,
            *[str(obj) for obj in objects],
        ])

        # Text labels must NOT be inside the flipped group
        labels = []

        # x-axis tick labels
        for x_tick in range(int(np.floor(x_min)), int(np.ceil(x_max)) + 1):
            labels.append(
                f'''
                <text x="{x_tick}" y="{svg_y(-0.25)}"
                      font-size="0.18" text-anchor="middle" fill="black">
                    {x_tick}
                </text>
                '''
            )

        # y-axis tick labels
        for y_tick in range(int(np.floor(y_min)), int(np.ceil(y_max)) + 1):
            labels.append(
                f'''
                <text x="-0.18" y="{svg_y(y_tick) + 0.06}"
                      font-size="0.18" text-anchor="end" fill="black">
                    {y_tick}
                </text>
                '''
            )

        # Axis names
        labels.append(
            f'''
            <text x="{x_max - 0.25}" y="{svg_y(-0.45)}"
                  font-size="0.22" text-anchor="middle" fill="black">
                x
            </text>
            '''
        )

        labels.append(
            f'''
            <text x="0.25" y="{svg_y(y_max - 0.25)}"
                  font-size="0.22" text-anchor="middle" fill="black">
                y
            </text>
            '''
        )

        # Optional title
        if title is not None:
            labels.append(
                f'''
                <text x="{(x_min + x_max) / 2}" y="{svg_y(y_max) + 0.28}"
                      font-size="0.24" text-anchor="middle" fill="black">
                    {title}
                </text>
                '''
            )

        labels_content = "\n".join(labels)

        return f"""
        <svg
            viewBox="{x_min} {-y_max} {width} {height}"
            width="450"
            height="450"
            xmlns="http://www.w3.org/2000/svg"
            style="background:white;"
        >
            <g transform="scale(1,-1)">
                {scene_content}
            </g>

            {labels_content}
        </svg>
        """

    return (world,)


@app.cell
def _(mo, svg, world):
    mo.hstack(
        [
            # Display an empty world
            mo.Html(
                world([-3, 3, -2, 4])
            ),
            # Display a world with a black square on top of the landing pad
            mo.Html(
                world(
                    [-3, 3, -2, 4],
                    svg.rect(x=-1, y=0, width=2, height=2, fill="black"),
                )
            ),
            # Display a world with a red square in the top-left corner of the view box
            # and a blue square on the top-right corner of the view box.
            mo.Html(
                world(
                    [-3, 3, -2, 4],
                    svg.rect(x=-3, y=2, width=2, height=2, fill="red"),
                    svg.rect(x=1, y=2, width=2, height=2, fill="blue"),
                )
            )
        ],
        justify="space-around"
    )

    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Booster Drawing

    Create a `booster` function that:

    - takes the numeric arguments `x`, `y`, `theta` (in radians), `f` and `phi` (in radians)

    and returns

    - a SVG fragment that represents the body of the booster and the flame of its reactor.
    (The booster drawing can be very simple, for example a rectangle for the body and another one of a different color for the flame will be fine.)

    **Constraint:** make sure that

    - the orientation of the flame is correct,
    - its length is proportional to the force $f$,
    - the flame length is equal to $\ell/2$ when $f=Mg$.


    Test you function in the following scenarios:

    ```python
    mo.hstack(
        [
            mo.Html(
                world(
                    [-3, 3, -2, 4],
                    booster(0, l/2, 0, 0, 0),
                )
            ),
            mo.Html(
                world(
                    [-3, 3, -2, 4],
                    booster(0, l, 0, M * g, 0),
                )
            ),
            mo.Html(
                world(
                    [-3, 3, -2, 4],
                    booster(-l/2, l, np.pi / 4, 2 * M * g, np.pi / 2),
                )
            ),
        ],
        justify="space-around",
    )
    ```
    """)
    return


@app.cell
def _(M, g, l, np):
    def booster(x, y, theta, f, phi):
        body_width = 0.20
        body_length = l
        nose_height = 0.14
        nozzle_width = 0.10
        nozzle_height = 0.08

        # Longueur de flamme : l/2 quand f = M*g
        flame_length = 0.0 if M * g == 0 else (l / 2.0) * f / (M * g)
        flame_width = 0.22

        # Corps local : centre au milieu du booster
        y_bottom = -l / 2.0
        y_top = l / 2.0

        # Base / nozzle
        x_base = 0.0
        y_base = y_bottom - nozzle_height

        # Direction de la flamme (opposée à la poussée)
        dx = np.sin(phi)
        dy = -np.cos(phi)

        # Direction perpendiculaire
        nx = -dy
        ny = dx

        # Triangle de flamme
        x1 = x_base + (flame_width / 2.0) * nx
        y1 = y_base + (flame_width / 2.0) * ny

        x2 = x_base - (flame_width / 2.0) * nx
        y2 = y_base - (flame_width / 2.0) * ny

        x3 = x_base + flame_length * dx
        y3 = y_base + flame_length * dy

        theta_deg = theta * 180.0 / np.pi

        return f"""
        <g transform="translate({x},{y}) rotate({theta_deg})">
            <!-- Corps -->
            <rect
                x="{-body_width/2}"
                y="{y_bottom}"
                width="{body_width}"
                height="{body_length}"
                fill="#c9c9c9"
                stroke="#222"
                stroke-width="0.03"
                rx="0.03"
            />

            <!-- Tête -->
            <polygon
                points="
                    {-body_width/2},{y_top}
                    {body_width/2},{y_top}
                    0,{y_top + nose_height}
                "
                fill="#bdbdbd"
                stroke="#222"
                stroke-width="0.03"
            />

            <!-- Nozzle -->
            <polygon
                points="
                    {-nozzle_width/2},{y_bottom}
                    {nozzle_width/2},{y_bottom}
                    {nozzle_width/4},{y_bottom - nozzle_height}
                    {-nozzle_width/4},{y_bottom - nozzle_height}
                "
                fill="#666"
                stroke="#222"
                stroke-width="0.02"
            />

            <!-- Flamme -->
            <polygon
                points="{x1},{y1} {x2},{y2} {x3},{y3}"
                fill="#ff9800"
                stroke="#d62828"
                stroke-width="0.02"
                opacity="0.95"
            />
        </g>
        """

    return (booster,)


@app.cell
def _(M, booster, g, l, mo, np, world):
    mo.hstack(
        [
            mo.vstack(
                [
                    mo.Html(
                        world(
                            [-3, 3, -2, 4],
                            booster(0, l/2, 0, 0, 0),
                            title="",  # supprimé du haut
                        )
                    ),
                    mo.Html("<div style='text-align:center'>x=0.00, y=1.00, θ=0.00, f=0.00, φ=0.00</div>")
                ]
            ),

            mo.vstack(
                [
                    mo.Html(
                        world(
                            [-3, 3, -2, 4],
                            booster(0, l, 0, M * g, 0),
                            title="",
                        )
                    ),
                    mo.Html("<div style='text-align:center'>x=0.00, y=2.00, θ=0.00, f=1.00, φ=0.00</div>")
                ]
            ),

            mo.vstack(
                [
                    mo.Html(
                        world(
                            [-3, 3, -2, 4],
                            booster(-l/2, l, np.pi / 4, 2 * M * g, np.pi / 2),
                            title="",
                        )
                    ),
                    mo.Html("<div style='text-align:center'>x=-1.00, y=2.00, θ=0.79, f=2.00, φ=1.57</div>")
                ]
            ),
        ],
        justify="space-around",
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Booster Animation

    Create a `booster_anim` function whose arguments are:

    - `x`, `y`, `theta` (in radians), `f` and `phi` (in radians)
    **which are functions of a time `t`**.
    - an animation duration `T`,

    and returns

    - a SVG fragment that represents the animated body of the booster and the flame of its reactor during `T` seconds, then repeats.
    (The booster drawing can be very simple, for example a rectangle for the body and another one of a different color for the flame will be fine.)

    **Constraint:** make sure that

    - the orientation of the flame is correct,
    - its length is proportional to the force $f$,
    - the flame length is equal to $\ell/2$ when $f=Mg$.

    Test your function in the following scenario:

    ```python
    def booster_anim_0():
        T = 5.0
        def x(t):
            return -l/2 + l * (t / T)
        def y(t):
            return l/2 + l/2 * (t / T)
        def theta(t):
            return (t / T) * 2 * np.pi
        def f(t):
            return M * g * (t / T)
        def phi(t):
            return 2 * np.pi * (t / T)
        return booster_anim(x, y, theta, f, phi, T=T)

    mo.Html(
        world([-3, 3, -2, 4], booster_anim_0())
    ).center()
    ```
    """)
    return


@app.cell
def _(M, g, l, np):
    def booster_anim(x, y, theta, f, phi, T=5.0, N=80):
        ts = np.linspace(0.0, T, N)

        body_width = 0.20
        body_length = l
        nozzle_width = 0.10
        nozzle_height = 0.08

        y_bottom = -l / 2.0
        y_top = l / 2.0

        flame_width = 0.22

        def flame_points(fi, phii):
            if M * g == 0:
                flame_length = 0.0
            else:
                flame_length = (l / 2.0) * fi / (M * g)

            x_base = 0.0
            y_base = y_bottom - nozzle_height

            dx = np.sin(phii)
            dy = -np.cos(phii)

            nx = -dy
            ny = dx

            x1 = x_base + (flame_width / 2.0) * nx
            y1 = y_base + (flame_width / 2.0) * ny

            x2 = x_base - (flame_width / 2.0) * nx
            y2 = y_base - (flame_width / 2.0) * ny

            x3 = x_base + flame_length * dx
            y3 = y_base + flame_length * dy

            return f"{x1},{y1} {x2},{y2} {x3},{y3}"

        translate_values = ";".join(
            f"{x(t)},{y(t)}"
            for t in ts
        )

        rotate_values = ";".join(
            f"{theta(t) * 180.0 / np.pi}"
            for t in ts
        )

        flame_values = ";".join(
            flame_points(f(t), phi(t))
            for t in ts
        )

        first_x = x(0.0)
        first_y = y(0.0)
        first_theta = theta(0.0) * 180.0 / np.pi
        first_flame = flame_points(f(0.0), phi(0.0))

        return f"""
        <g transform="translate({first_x},{first_y})">
            <animateTransform
                attributeName="transform"
                type="translate"
                values="{translate_values}"
                dur="{T}s"
                repeatCount="indefinite"
            />

            <g transform="rotate({first_theta})">
                <animateTransform
                    attributeName="transform"
                    type="rotate"
                    values="{rotate_values}"
                    dur="{T}s"
                    repeatCount="indefinite"
                />

                <!-- Corps du booster -->
                <rect
                    x="{-body_width/2}"
                    y="{y_bottom}"
                    width="{body_width}"
                    height="{body_length}"
                    fill="#c9c9c9"
                    stroke="#222"
                    stroke-width="0.03"
                    rx="0.03"
                />

                <!-- Nozzle -->
                <polygon
                    points="
                        {-nozzle_width/2},{y_bottom}
                        {nozzle_width/2},{y_bottom}
                        {nozzle_width/4},{y_bottom - nozzle_height}
                        {-nozzle_width/4},{y_bottom - nozzle_height}
                    "
                    fill="#666"
                    stroke="#222"
                    stroke-width="0.02"
                />

                <!-- Flamme animée -->
                <polygon
                    points="{first_flame}"
                    fill="#ff9800"
                    stroke="#d62828"
                    stroke-width="0.02"
                    opacity="0.95"
                >
                    <animate
                        attributeName="points"
                        values="{flame_values}"
                        dur="{T}s"
                        repeatCount="indefinite"
                    />
                </polygon>
            </g>
        </g>
        """

    return (booster_anim,)


@app.cell
def _(M, booster_anim, g, l, mo, np, world):
    def booster_anim_0():
        T = 5.0

        def x(t):
            return -l/2 + l * (t / T)

        def y(t):
            return l/2 + l/2 * (t / T)

        def theta(t):
            return (t / T) * 2 * np.pi

        def f(t):
            return M * g * (t / T)

        def phi(t):
            return 2 * np.pi * (t / T)

        return booster_anim(x, y, theta, f, phi, T=T)

    mo.Html(
        world([-3, 3, -2, 4], booster_anim_0())
    ).center()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Animated Simulation Results

    Let's go back to a booster whose evolution is governed by its system of ordinary differentential equations. Produce a animation of the booster for 5 seconds for each of the following initial value problems:

    1. $(x, \dot{x}, y, \dot{y}, \theta, \dot{\theta}) = (0.0, 0.0, 10.0, 0.0, 0.0, 0.0)$, $f=0$ and $\phi=0$

    2. $(x, \dot{x}, y, \dot{y}, \theta, \dot{\theta}) = (0.0, 0.0, 10.0, 0.0, 0.0, 0.0)$, $f=Mg$ and $\phi=0$

    3. $(x, \dot{x}, y, \dot{y}, \theta, \dot{\theta}) = (0.0, 0.0, 10.0, 0.0, 0.0, 0.0)$, $f=Mg$ and $\phi=\pi/8$

    4. The "controlled landing" scenario (see above).
    """)
    return


@app.cell
def _(booster_anim, mo, redstart_solve, world):
    def animated_scenario(y0, f_phi, view_box=[-5, 5, -2, 12], T=5.0):
        t_span = [0.0, T]

        sol = redstart_solve(t_span, y0, f_phi)

        def x(t):
            return sol(t)[0]

        def y(t):
            return sol(t)[2]

        def theta(t):
            return sol(t)[4]

        def f(t):
            return f_phi(t, sol(t))[0]

        def phi(t):
            return f_phi(t, sol(t))[1]

        return mo.Html(
            world(
                view_box,
                booster_anim(x, y, theta, f, phi, T=T),
            )
        )

    return (animated_scenario,)


@app.cell
def _(animated_scenario, np):
    def animation_scenario_1():
        y0 = np.array([
            0.0,   # x
            0.0,   # vx
            10.0,  # y
            0.0,   # vy
            0.0,   # theta
            0.0,   # omega
        ])

        def f_phi(t, y):
            return np.array([0.0, 0.0])

        return animated_scenario(
            y0,
            f_phi,
            view_box=[-5, 5, -2, 12],
            T=5.0,
        )

    animation_scenario_1()
    return


@app.cell
def _(M, animated_scenario, g, np):
    def animation_scenario_2():
        y0 = np.array([
            0.0,   # x
            0.0,   # vx
            10.0,  # y
            0.0,   # vy
            0.0,   # theta
            0.0,   # omega
        ])

        def f_phi(t, y):
            return np.array([M * g, 0.0])

        return animated_scenario(
            y0,
            f_phi,
            view_box=[-5, 5, -2, 12],
            T=5.0,
        )

    animation_scenario_2()
    return


@app.cell
def _(M, animated_scenario, g, np):
    def animation_scenario_3():
        y0 = np.array([
            0.0,   # x
            0.0,   # vx
            10.0,  # y
            0.0,   # vy
            0.0,   # theta
            0.0,   # omega
        ])

        def f_phi(t, y):
            return np.array([M * g, np.pi / 8])

        return animated_scenario(
            y0,
            f_phi,
            view_box=[-5, 5, -2, 12],
            T=5.0,
        )

    animation_scenario_3()
    return


@app.cell
def _(animated_scenario, controlled_landing_force, np):
    def animation_scenario_4():
        y0 = np.array([
            0.0,   # x
            0.0,   # vx
            10.0,  # y
            -2.0,  # vy
            0.0,   # theta
            0.0,   # omega
        ])

        def f_phi(t, y):
            return np.array([controlled_landing_force(t), 0.0])

        return animated_scenario(
            y0,
            f_phi,
            view_box=[-5, 5, -2, 12],
            T=5.0,
        )

    animation_scenario_4()
    return


if __name__ == "__main__":
    app.run()
