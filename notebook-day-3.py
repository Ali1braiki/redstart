import marimo

__generated_with = "0.20.4"
app = marimo.App(app_title="")


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

    return la, np, plt, sci, scipy


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

    Define the Python constants `g`, `M` and `l` that correspond to the gravity constant, the mass and length of the booster.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### 🔓 Solution
    """)
    return


@app.cell(hide_code=True)
def _():
    g = 1.0
    M = 1.0
    l = 2
    return M, g, l


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Forces

    Compute the cartesian coordinates $f_x$ and $f_y$ of the force applied to the booster by the reactor, as functions of $f$, $\theta$ and $\phi$.
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    ### 🔓 Solution
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Given the geometric setting, the cartesian coordinates of the unit vector $\vec{u}=(u_x, u_y)$ aligned with the reactor (or flame) axis and pointing from the reactor towards the flame satisfy:

    \begin{align*}
    u_x & = +\sin (\theta + \phi) \\
    u_y & = -\cos(\theta +\phi)
    \end{align*}

    Assuming that $f \geq 0$, the force applied to the booster is in the opposite direction and has amplitude $f$:

    $$
    \vec{f} = -f \vec{u}
    $$

    Therefore,

    \begin{align*}
    f_x & = -f \sin (\theta + \phi) \\
    f_y & = +f \cos(\theta +\phi)
    \end{align*}
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Center of Mass

    Give the ordinary differential equation that governs the evolution of the position $(x, y)$ of the center of mass of the booster.
    """)
    return


@app.cell
def _(mo):
    mo.md("""
    ### 🔓 Solution
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The force exerted by the gravity on the booster is

    $$
    \vec{f}_g =
    \begin{bmatrix}
    0 \\ - M g
    \end{bmatrix}
    $$

    By Newton's second law of motion, the acceleration $\vec{a} = (\ddot{x}, \ddot{y})$
    satisfies $M \vec{a} = \vec{f} + \vec{f}_g$ and thus

    \begin{align*}
    M \ddot{x} & = -f \sin (\theta + \phi) \\
    M \ddot{y} & = +f \cos(\theta +\phi) - Mg
    \end{align*}
    """)
    return


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
    ### 🔓 Solution

    The moment of inertia of a thin rod with uniformly distributed mass about its center is of mass is

    $$
    J = \frac{1}{12} M \ell^2
    $$
    """)
    return


@app.cell
def _(M, l):
    J = M * l ** 2 / 12
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
    ### 🔓 Solution

    Newton's Second Law for Rotation is $J \ddot{\theta} = \tau$ where $\tau$ is the torque applied to the booster. Here the torque applied by the gravity to the booster is $0$ by symmetry and only the booster reactor induces a torque. The torque can be
    first computed as a vector in 3D as the cross-product of the vector between the center of the booster and the reactor location and the force applied by the reactor.
    Afterwards, we can be project it on the 3rd axis to get $\tau$.

    Thus, we have

    $$
    \tau =
    \left(
    \ell / 2
    \begin{bmatrix}
    {} +\sin \theta \\ - \cos \theta \\ 0
    \end{bmatrix}
    \wedge \begin{bmatrix} -f \sin (\theta + \phi) \\ +f \cos (\theta + \phi) \\ 0
    \end{bmatrix}
    \right)
    \cdot \begin{bmatrix} 0 \\ 0 \\ 1 \end{bmatrix}
    =
    \ell/2 (f\sin \theta \cos (\theta + \phi) - f\sin (\theta + \phi) \cos \theta).
    $$

    Since $\sin \alpha \cos \beta - \sin \beta \cos \alpha = \sin (\alpha - \beta)$,
    we obtain

    $$
    \tau = - f (\ell/2) \sin \phi,
    $$

    thus the angular acceleration is governed by

    $$
    J \ddot{\theta} = - f (\ell / 2)  \sin \phi.
    $$
    """)
    return


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
    ### 🔓 Solution

    Given that

    \begin{align*}
    M \ddot{x} & = -f \sin (\theta + \phi) \\
    M \ddot{y} & = +f \cos(\theta +\phi) - Mg \\
    J \ddot{\theta} & = - f (\ell/2) \sin \phi
    \end{align*}

    and $\dot{x} = v_x$, $\dot{y} = v_y$ and $\dot{\theta} = \omega$, we
    can use as a state vector $s = (x, v_x, y, v_y, \theta, \omega) \in \mathbb{R}^6$
    and the corresponding function $F$ is given by

    $$
    F(s, f, \phi) = \begin{bmatrix}
    v_x \\ -(f / M) \sin (\theta + \phi) \\
    v_y \\ +(f / M) \cos(\theta +\phi) - g \\
    \omega \\ - (f / J) (\ell/2) \sin \phi
    \end{bmatrix}
    $$
    """)
    return


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


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### 🔓 Solution
    """)
    return


@app.cell(hide_code=True)
def _(J, M, g, l, np, scipy):
    def redstart_solve(t_span, y0, f_phi):
        def fun(t, state):
            x, vx, y, vy, theta, omega = state
            f, phi = f_phi(t, state)
            d2x = (-f * np.sin(theta + phi)) / M
            d2y = (+ f * np.cos(theta + phi)) / M - g
            d2theta = - (f / J) * (l / 2) * np.sin(phi)
            return np.array([vx, d2x, vy, d2y, omega, d2theta])
        r = scipy.integrate.solve_ivp(fun, t_span, y0, dense_output=True)
        return r.sol

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


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 🔓 Solution

    In the free fall scenario, the solution satisfies $x(t)=0$, $y(t) = y(0) - g/2 t^2$ and $\theta(t) = 0$. Since numerically $y(0)=10.0$, $g=1$ and $\ell=2$, the threshold
    is crossed when $10 - 1/2 t^2 = 2$, that is $t=4$.
    """)
    return


@app.cell(hide_code=True)
def _(l, np, plt, redstart_solve):
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
    mo.md("""
    ### 🔓 Solution
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We can search for a cubic polynomial

    $$
    y(t) = a_3 t^3 + a_2 t^2 + a_1 t + a_0
    $$

    that solves the four given constraints,
    then deduce $f(t)$ from the equation $M \ddot{y} = f + Mg$.

    The time derivative of $y$ satisfies
    $$
    \dot{y}(t) = 3 a_3 t^2 + 2 a_2 t + a_1,
    $$
    thus the constraints are:

    \begin{align*}
    y(0) = a_0 &= 10, \\
    \dot{y}(0) = a_1 &= -2,\\
    y(5) = 125 a_3 + 25 a_2 + 5 a_1 + a_0 &= 1, \\
    \dot{y}(5) = 75 a_3 + 10 a_2 + a_1 &= 0. \\
    \end{align*}

    The solution of this linear system provides:

    $$
    y(t)
    =\frac{8}{125}t^3 - \frac{7}{25} t^2 - 2t + 10,
    $$
    which yields
    $$
    \ddot{y}(t)
    =
    \frac{48}{125}t - \frac{14}{25}
    $$
    and therefore since $M=1$ and $g=1$,
    $$
    f(t) = \frac{\ddot{y}(t)}{M} + g = \frac{48}{125}t + \frac{11}{25}.
    $$
    """)
    return


@app.cell(hide_code=True)
def _(l, np, plt, redstart_solve):
    def controlled_landing_example():
        t_span = [0.0, 5.0]
        y0 = [0.0, 0.0, 10.0, -2.0, 0.0, 0.0]
        def f_phi_smooth_landing(t, state):
            return np.array([48 / 125 * t + 11 / 25, 0])
        sol = redstart_solve(t_span, y0, f_phi=f_phi_smooth_landing)
        t = np.linspace(t_span[0], t_span[1], 1000)
        y_t = sol(t)[2]
        plt.plot(t, y_t, label=r"$y(t)$ (height in meters)")
        plt.plot(t, (l / 2) * np.ones_like(t), color="grey", ls="--", label=r"$y=\ell/2$")
        plt.title("Controlled Landing")
        plt.xlabel("time $t$")
        plt.grid(True)
        plt.legend()
        return plt.gcf()
    controlled_landing_example()
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

    return animate_transform, svg, transform


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


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### 🔓 Solution
    """)
    return


@app.cell
def _(svg, transform):
    def world(view_box, *objects):
        x_min, x_max, y_min, y_max = view_box    
        width, height = x_max - x_min, y_max - y_min

        return svg.svg(
          xmlns="http://www.w3.org/2000/svg",
          viewBox=f"0 0 {width} {height}",
          style="max-height:80vh")(
              transform.translate(x=-x_min, y=y_max)(
                  transform.scale(y=-1.0)(
                      # Sky
                      svg.rect(x=-1e3, y=0, width=2e3, height=1e3, fill="lightskyblue"),
                      # Ground
                      svg.rect(x=-1e3, y=-2e3, width=2e3, height=2e3, fill="sandybrown"),
                      # Target 
                      svg.rect(x=-1, y =-1, width=2, height=1, fill="lightgreen"),
                      *objects,
                )
            )
        )

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


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### 🔓 Solution
    """)
    return


@app.cell
def _(M, g, l, np, svg, transform):
    def booster(x, y, theta, f, phi):
        flame_length = (l / 2) * (f / M / g)
        return transform.translate(x, y)(
            transform.rotate(theta / np.pi * 180.0)(
                svg.rect(x=-l/20, y=-l/2, width=l/10, height=l, fill="black"),
                transform.translate(0, -l / 2)(
                    transform.rotate(phi / np.pi * 180)(
                        svg.rect(
                            x=-l/20,
                            y=-flame_length,
                            width=l/10,
                            height=flame_length,
                            fill="red",
                        )
                    )
                )
            )
        )

    return (booster,)


@app.cell(hide_code=True)
def _(M, booster, g, l, mo, np, world):
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


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### 🔓 Solution
    """)
    return


@app.cell
def _(M, animate_transform, g, l, np, svg):
    def booster_anim(x, y, theta, f, phi, T):
        if not callable(theta):
            theta_cst = theta
            theta = lambda t: theta_cst
        if not callable(phi):
            phi_cst = phi
            phi = lambda t: phi_cst

        def theta_deg(t):
            return theta(t) / np.pi * 180.0

        def phi_deg(t):
            return phi(t) / np.pi * 180.0

        return animate_transform.translate(x, y, T=T)(
            animate_transform.rotate(theta_deg, T=T)(
                svg.rect(
                    x=-l / 20,
                    y=-l/2,
                    width=l / 10,
                    height=l,
                    fill="black",
                ),
                animate_transform.translate(y=-l/2, T=T)(
                    animate_transform.rotate(phi_deg, T=T)(
                        animate_transform.scale(y=f, T=T)(
                            svg.rect(
                                x=-l/20,
                                y=-1/M/g,
                                width=l / 10,
                                height=1/M/g,
                                fill="red",
                            )
                        )
                    )
                ),
            )
        )

    return (booster_anim,)


@app.cell
def _(M, booster_anim, g, l, np):
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

    return (booster_anim_0,)


@app.cell
def _(booster_anim_0, mo, world):
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


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### 🔓 Solution
    """)
    return


@app.cell
def _(booster_anim, mo, np, redstart_solve, world):
    def anim_1():
        t_span = [0.0, 5.0]
        y0 = [0.0, 0.0, 10.0, 0.0, 0.0, 0.0] 
        def f_phi(t, state):
            return np.array([0, 0])
        sol = redstart_solve(t_span, y0, f_phi)
        x = lambda t: sol(t)[0]
        y = lambda t: sol(t)[2]
        theta = lambda t : sol(t)[4]
        f = lambda t: f_phi(t, sol(t))[0]
        phi = lambda t: f_phi(t, sol(t))[0]
        return mo.Html(
            world(
                [-3, 3, -2, 12], 
                booster_anim(x, y, theta, f, phi, T=t_span[1])
            )
        ).center()

    anim_1()
    return


@app.cell
def _(M, booster_anim, g, mo, np, redstart_solve, world):
    def anim_2():
        t_span = [0.0, 5.0]
        y0 = [0.0, 0.0, 10.0, 0.0, 0.0, 0.0]
        def f_phi(t, state):
            return np.array([M * g, 0])
        sol = redstart_solve(t_span, y0, f_phi)
        x = lambda t: sol(t)[0]
        y = lambda t: sol(t)[2]
        theta = lambda t : sol(t)[4]
        f = lambda t: f_phi(t, sol(t))[0]
        phi = lambda t: f_phi(t, sol(t))[1]
        return mo.Html(
            world(
                [-3, 3, -2, 12], 
                booster_anim(x, y, theta, f, phi, T=t_span[1])
            )
        ).center()

    anim_2()
    return


@app.cell
def _(M, booster_anim, g, mo, np, redstart_solve, world):
    def anim_3():
        t_span = [0.0, 5.0]
        y0 = [0.0, 0.0, 10.0, 0.0, 0.0, 0.0]
        def f_phi(t, state):
            return np.array([M * g, np.pi / 8])
        sol = redstart_solve(t_span, y0, f_phi)
        x = lambda t: sol(t)[0]
        y = lambda t: sol(t)[2]
        theta = lambda t : sol(t)[4]
        f = lambda t: f_phi(t, sol(t))[0]
        phi = lambda t: f_phi(t, sol(t))[1]
        return mo.Html(
            world(
                [-3, 3, -2, 12], 
                booster_anim(x, y, theta, f, phi, T=t_span[1])
            )
        ).center()

    anim_3()
    return


@app.cell
def _(booster_anim, mo, np, redstart_solve, world):
    def anim_4():
        t_span = [0.0, 5.0]
        y0 = [0.0, 0.0, 10.0, -2.0, 0.0, 0.0]
        def f_phi(t, state):
            return np.array([48 / 125 * t + 11 / 25, 0])
        sol = redstart_solve(t_span, y0, f_phi)
        x = lambda t: sol(t)[0]
        y = lambda t: sol(t)[2]
        theta = lambda t : sol(t)[4]
        f = lambda t: f_phi(t, sol(t))[0]
        phi = lambda t: f_phi(t, sol(t))[1]
        return mo.Html(
            world(
                [-3, 3, -2, 12], 
                booster_anim(x, y, theta, f, phi, T=t_span[1])
            )
        ).center()

    anim_4()
    return


@app.cell
def _(mo):
    mo.md(r"""
    # Linearized Dynamics
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Equilibria

    We assume that

    - $|\theta| < \pi/2$,
    - $|\phi| < \pi/2$, and
    - $f > 0$.

    What are the possible equilibria of the system for constant inputs $f$ and $\phi$ and what are the corresponding values of these inputs?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### 🔓 Solution
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Our state is $s = (x, v_x, y, v_y,\theta, \omega)$ and the system is governed by
    $\dot{s} = F(s, f, \phi)$ with
    $$
    F(s, f, \phi) = \begin{bmatrix}
    v_x \\ -(f / M) \sin (\theta + \phi) \\
    v_y \\ +(f / M) \cos(\theta +\phi) - g \\
    \omega \\ - (f / J) (\ell/2) \sin \phi
    \end{bmatrix}
    $$
    The equilibria are characterized by $F(s, f, \phi) = 0$. We obtain directly that
    $v_x = v_y = 0$ and $\omega = 0$. We also extract the two equations

    $$
    \begin{bmatrix}
    -(f / M) \sin (\theta + \phi) \\
    +(f / M) \cos(\theta +\phi)
    \end{bmatrix}
    =
    \begin{bmatrix}
    0 \\
    g
    \end{bmatrix}
    $$
    which holds if when $|\theta| < \pi/2$ and $|\phi| < \pi/2$ and only if
    $\theta = \phi = 0$ and $f = M g$. The final equation is then satisfied if and only if
    $\omega = 0$. Finally, we obtain the equilibria as:
    $$
    \begin{bmatrix}
    x \\
    v_x \\
    y \\
    v_y \\
    \theta \\
    \omega \\
    f \\
    \phi
    \end{bmatrix}
    =
    \begin{bmatrix}
    ? \\
    0 \\
    ? \\
    0 \\
    0 \\
    0 \\
    M g \\
    0
    \end{bmatrix}
    $$
    where $?$ stands for "any possible value".
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Linearized Model

    Introduce the error variables $\Delta x$, $\Delta y$, $\Delta \theta$, and $\Delta f$ and $\Delta \phi$ of the state and input values with respect to the generic equilibrium configuration.
    What are the linear ordinary differential equations that govern (approximately) these variables in a neighbourhood of the equilibrium?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### 🔓 Solution
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We have $\Delta \theta = \theta$, $\Delta \phi = \phi$ and $\Delta f = f - M g$. Given that

    \begin{align*}
    M \ddot{x} & = -f \sin (\theta + \phi) \\
    M \ddot{y} & = +f \cos(\theta +\phi) - Mg \\
    J \ddot{\theta} & = - f (\ell/2) \sin \phi
    \end{align*}

    and that for small values of $\alpha$, $\sin \alpha \approx \alpha$ and $\cos \alpha \approx 1$, we obtain:

    \begin{align*}
    M (d/dt)^2 \Delta x &= - Mg (\Delta \theta + \Delta \phi)  \\
    M (d/dt)^2 \Delta y &= \Delta f \\
    J (d/dt)^2 \Delta \theta &= - (Mg \ell /2) \Delta \phi \\
    \end{align*}
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Standard Form

    1. What are the matrices $A$ and $B$ associated to this linear model in standard form?
    2. Define the corresponding NumPy arrays `A` and `B`.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 🔓 Solution
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Note: remember that $J = (1/12) M \ell^2$.

    $$
    A =
    \begin{bmatrix}
    0 & 1 & 0 & 0 & 0  & 0 \\
    0 & 0 & 0 & 0 & -g & 0 \\
    0 & 0 & 0 & 1 & 0  & 0 \\
    0 & 0 & 0 & 0 & 0  & 0 \\
    0 & 0 & 0 & 0 & 0  & 1 \\
    0 & 0 & 0 & 0 & 0  & 0
    \end{bmatrix}
    \;\;\;
    B =
    \begin{bmatrix}
    0 & 0\\
    0 & -g\\
    0 & 0\\
    1/M & 0\\
    0 & 0 \\
    0 & -M g \ell/(2J)\\
    \end{bmatrix}
    =
    \begin{bmatrix}
    0 & 0\\
    0 & -g\\
    0 & 0\\
    1/M & 0\\
    0 & 0 \\
    0 & - 6 g / \ell\\
    \end{bmatrix}
    $$
    """)
    return


@app.cell(hide_code=True)
def _(g, np):
    A = np.zeros((6, 6))
    A[0, 1] = 1.0
    A[1, 4] = -g
    A[2, 3] = 1.0
    A[4, -1] = 1.0
    A
    return (A,)


@app.cell(hide_code=True)
def _(M, g, l, np):
    B = np.zeros((6, 2))
    B[ 1, 1]  = -g 
    B[ 3, 0]  = 1/M
    B[-1, 1] = -6 * g / l
    B
    return (B,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Stability

    Is the generic equilibrium asymptotically stable?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 🔓 Solution

    No, since $0$ is the only eigenvalue of $A$ and $0$ doesn't have a negative real part.
    """)
    return


@app.cell(hide_code=True)
def _(A, la):
    eigenvalues, eigenvectors = la.eig(A)
    print(f"Eigenvalues of A: {eigenvalues}")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Controllability

    Is the linearized model controllable?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 🔓 Solution

    The controllability matrix of the system is:
    """)
    return


@app.cell(hide_code=True)
def _(A, B, np):
    # Controllability
    cs = np.column_stack
    mp = np.linalg.matrix_power
    KC = cs([mp(A, k) @ B for k in range(6)])
    KC
    return (KC,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    and its rank is
    """)
    return


@app.cell(hide_code=True)
def _(KC, np):
    int(np.linalg.matrix_rank(KC))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    which is equal to the state dimension, so the answer is yes, it's controllable.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Lateral Dynamics

    We limit our interest in the lateral position $x$, the tilt $\theta$ and their derivatives (we are for the moment fine with letting $y$ and $\dot{y}$ be uncontrolled). We also set $f = M g$ and control the system only with $\phi$.

    - What are the new (reduced) matrices $A$ and $B$ for this reduced system?

    - Check the controllability of this new system.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 🔓 Solution
    """)
    return


@app.cell
def _(g, l, np):
    A_lat = np.array([
        [0, 1, 0, 0], 
        [0, 0, -g, 0], 
        [0, 0, 0, 1], 
        [0, 0, 0, 0]], dtype=np.float64)
    B_lat = np.array([[0, -g, 0, - 6 * g / l]]).T

    print("A_lat:")
    print(A_lat)
    print("B_lat:")
    print(B_lat)
    return A_lat, B_lat


@app.cell(hide_code=True)
def _(A_lat, B_lat, np):
    # Controllability
    _cs = np.column_stack
    _mp = np.linalg.matrix_power
    KC_lat = _cs([_mp(A_lat, k) @ B_lat for k in range(6)])
    KC_lat
    return (KC_lat,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    This reduced system of dimension 4 is controllable since the rank of its controllability matrix is 4:
    """)
    return


@app.cell(hide_code=True)
def _(KC_lat, np):
    np.linalg.matrix_rank(KC_lat)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Linear Model in Free Fall

    Make graphs of $x(t)$ and $\theta(t)$ for the linearized model when
    - $x(0)=0$, $\dot{x}(0)=0$, $\theta(0) = \pi/4$, $\dot{\theta}(0) =0$, and
    - $\phi(t)=0$ at all times.

    What do you see? How do you explain it?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 🔓 Solution
    """)
    return


@app.cell(hide_code=True)
def _(g, l, np):
    def make_fun_lat(phi):
        def fun_lat(t, state):
            x, dx, theta, dtheta = state
            phi_ = phi(t, state)
            d2x = -g * (theta + phi_)
            d2theta = - 6 * g / l * phi_
            return np.array([dx, d2x, dtheta, d2theta])

        return fun_lat

    return (make_fun_lat,)


@app.cell(hide_code=True)
def _(make_fun_lat, mo, np, plt, sci):
    def lin_sim_1():
        def phi(t, state):
            return 0.0

        f_lat = make_fun_lat(phi)
        t_span = [0, 10]
        state_0 = [0, 0, 45 * np.pi / 180.0, 0]
        r = sci.solve_ivp(
            fun=f_lat, y0=state_0, t_span=t_span, dense_output=True
        )
        t = np.linspace(t_span[0], t_span[1], 1000)
        sol_t = r.sol(t)
        fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True)
        ax1.plot(t, sol_t[0], label=r"$x(t)$")
        ax1.grid(True)
        ax1.legend()
        ax2.plot(t, sol_t[2], label=r"$\theta(t)$")
        ax2.grid(True)
        ax2.set_xlabel(r"time $t$")
        ax2.legend()
        return mo.center(fig)


    lin_sim_1()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    - Since the reactor pushes (with a constant force) in the axis of the booster ($\phi=0$) and the initial title velocity $\omega = \dot{\theta}$ is zero, it's sensible that the title $\theta$ stays constant. That explains the second graph.
    - On the other hand, the constant projected force on the $x$-axis drives a constant acceleration which is towards the left since the initial tilt is positive. That explain the first graph.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Manually Tuned Controller

    Try to find the two missing coefficients of the matrix

    $$
    K =
    \begin{bmatrix}
    0 & 0 & ? & ?
    \end{bmatrix}
    \in \mathbb{R}^{4\times 1}
    $$

    such that the control law

    $$
    \Delta \phi(t) = - K \cdot
    \begin{bmatrix}
    \Delta x(t) \\
    \Delta \dot{x}(t) \\
    \Delta \theta(t) \\
    \Delta \dot{\theta}(t)
    \end{bmatrix} \in \mathbb{R}
    $$

    manages  when
    $\Delta x(0)=0$, $\Delta \dot{x}(0)=0$, $\Delta \theta(0) = 45 / 180  \times \pi$  and $\Delta \dot{\theta}(0) =0$ to:

    - make $\Delta \theta(t) \to 0$ in approximately $20$ sec (or less),
    - $|\Delta \theta(t)| < \pi/2$ and $|\Delta \phi(t)| < \pi/2$ at all times,
    - (but we don't care about a possible drift of $\Delta x(t)$).

    Explain your thought process, show your iterative guesses and simulations!

    Is your final closed-loop model asymptotically stable?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### 🔓 Solution
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We try first a controller that corrects using only $\Delta \theta$ since it it's the simples think we can think of (a controller based only on the derivative would not achieve $\Delta \theta(t) \to 0$ since it would only knows $\Delta \theta(t)$ up to a constant). When $\Delta \theta > 0$, we want the reactor to be oriented on the right ($\Delta \phi > 0$) to compensate for this trend.

    Hence it makes sens to start for something simple such as
    $\Delta \phi =  \Delta \theta$, which corresponds to

    $$
    K =
    \begin{bmatrix}
    0 & 0 & -1 & 0
    \end{bmatrix}
    \in \mathbb{R}^{4\times 1}
    $$

    and

    $$
    \Delta \phi(t) = - K \cdot
    \begin{bmatrix}
    \Delta x(t) \\
    \Delta \dot{x}(t) \\
    \Delta \theta(t) \\
    \Delta \dot{\theta}(t)
    \end{bmatrix} \in \mathbb{R}
    $$

    Let's make a simulation out of this!
    """)
    return


@app.cell
def _(A_lat, B_lat, make_fun_lat, mo, np, plt, sci):
    def lin_sim_k1():

        K = np.array([0.0, 0.0, -1.0, 0.0])

        print(
            "eigenvalues:",
            np.linalg.eig(
                A_lat - B_lat.reshape((-1, 1)) @ K.reshape((1, -1))
            ).eigenvalues,
        )

        t_span = [0, 20.0]
        t = np.linspace(t_span[0], t_span[1], 1000)
        state_0 = [0, 0, 45 * np.pi / 180.0, 0]

        def phi(t, state):
            return -K.dot(state)

        f_lat = make_fun_lat(phi)
        r = sci.solve_ivp(fun=f_lat, y0=state_0, t_span=t_span, dense_output=True)
        sol_lin_t = r.sol(t)

        fig, (ax1, ax2, ax3) = plt.subplots(3, 1, sharex=True, figsize=(12, 6))
        ax1.plot(t, sol_lin_t[0], label=r"$x(t)$ (lin.)")
        ax1.grid(True)
        ax1.legend(loc="lower right")
        ax2.plot(t, sol_lin_t[2], label=r"$\theta(t)$ (lin.)")
        ax2.plot(t, 0.5 * np.pi * np.ones_like(t), "r--", label=r"$\pm\pi/2$")
        ax2.plot(t, -0.5 * np.pi * np.ones_like(t), "r--")
        ax2.grid(True)
        ax2.legend(loc="lower right")
        ax3.plot(t, phi(t, sol_lin_t), label=r"$\phi(t)$ (lin.)")
        ax3.grid(True)
        ax3.plot(t, 0.5 * np.pi * np.ones_like(t), "r--", label=r"$\pm\pi/2$")
        ax3.plot(t, -0.5 * np.pi * np.ones_like(t), "r--")
        ax3.set_xlabel(r"time $t$")
        ax3.legend(loc="lower right")
        return mo.center(fig)


    lin_sim_k1()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Unfortunately that doesn't work, we have introduced an oscillatory dynamics.

    To correct that, we may introduce some additionial "friction" that prevents our compensation to kick in too fast and end up the control
    $\Delta \phi = \Delta \theta + \beta (d \Delta \theta /dt)$, for some $\beta > 0$, which corresponds to

    $$
    K =
    \begin{bmatrix}
    0 & 0 & -1 & -\beta
    \end{bmatrix}
    \in \mathbb{R}^{4\times 1}
    $$

    Experimentally (see below), anything between $\beta = 0.1$ and $\beta = 5.0$ seems to satisfy the specification. The closed-loop dynamics is slower need $0.1$ and faster near $5.0$.

    In any case, there is a permament drift which is induced on $\Delta x$, which does not converge to $0$. This is corroborated by a double eigenvalue at $0$, which proves that our closed-loop dynamics is **not** asymptotically stable.
    """)
    return


@app.cell(hide_code=True)
def _(A_lat, B_lat, make_fun_lat, mo, np, plt, sci):
    def lin_sim_k2():

        K = np.array([0.0, 0.0, -1.0, -0.1])

        print(
            "eigenvalues:",
            np.linalg.eig(
                A_lat - B_lat.reshape((-1, 1)) @ K.reshape((1, -1))
            ).eigenvalues,
        )

        t_span = [0, 20.0]
        t = np.linspace(t_span[0], t_span[1], 1000)
        state_0 = [0, 0, 45 * np.pi / 180.0, 0]

        def phi(t, state):
            return -K.dot(state)

        f_lat = make_fun_lat(phi)
        r = sci.solve_ivp(fun=f_lat, y0=state_0, t_span=t_span, dense_output=True)
        sol_lin_t = r.sol(t)

        fig, (ax1, ax2, ax3) = plt.subplots(3, 1, sharex=True, figsize=(12, 6))
        ax1.plot(t, sol_lin_t[0], label=r"$x(t)$ (lin.)")
        ax1.grid(True)
        ax1.legend(loc="lower right")
        ax2.plot(t, sol_lin_t[2], label=r"$\theta(t)$ (lin.)")
        ax2.plot(t, 0.5 * np.pi * np.ones_like(t), "r--", label=r"$\pm\pi/2$")
        ax2.plot(t, -0.5 * np.pi * np.ones_like(t), "r--")
        ax2.grid(True)
        ax2.legend(loc="lower right")
        ax3.plot(t, phi(t, sol_lin_t), label=r"$\phi(t)$ (lin.)")
        ax3.grid(True)
        ax3.plot(t, 0.5 * np.pi * np.ones_like(t), "r--", label=r"$\pm\pi/2$")
        ax3.plot(t, -0.5 * np.pi * np.ones_like(t), "r--")
        ax3.set_xlabel(r"time $t$")
        ax3.legend(loc="lower right")
        return mo.center(fig)


    lin_sim_k2()
    return


@app.cell
def _(A_lat, B_lat, make_fun_lat, mo, np, plt, sci):
    def lin_sim_k3():

        K = np.array([0.0, 0.0, -1.0, -5.0])

        print(
            "eigenvalues:",
            np.linalg.eig(
                A_lat - B_lat.reshape((-1, 1)) @ K.reshape((1, -1))
            ).eigenvalues,
        )

        t_span = [0, 20.0]
        t = np.linspace(t_span[0], t_span[1], 1000)
        state_0 = [0, 0, 45 * np.pi / 180.0, 0]

        def phi(t, state):
            return -K.dot(state)

        f_lat = make_fun_lat(phi)
        r = sci.solve_ivp(fun=f_lat, y0=state_0, t_span=t_span, dense_output=True)
        sol_lin_t = r.sol(t)

        fig, (ax1, ax2, ax3) = plt.subplots(3, 1, sharex=True, figsize=(12, 6))
        ax1.plot(t, sol_lin_t[0], label=r"$x(t)$ (lin.)")
        ax1.grid(True)
        ax1.legend(loc="lower right")
        ax2.plot(t, sol_lin_t[2], label=r"$\theta(t)$ (lin.)")
        ax2.plot(t, 0.5 * np.pi * np.ones_like(t), "r--", label=r"$\pm\pi/2$")
        ax2.plot(t, -0.5 * np.pi * np.ones_like(t), "r--")
        ax2.grid(True)
        ax2.legend(loc="lower right")
        ax3.plot(t, phi(t, sol_lin_t), label=r"$\phi(t)$ (lin.)")
        ax3.grid(True)
        ax3.plot(t, 0.5 * np.pi * np.ones_like(t), "r--", label=r"$\pm\pi/2$")
        ax3.plot(t, -0.5 * np.pi * np.ones_like(t), "r--")
        ax3.set_xlabel(r"time $t$")
        ax3.legend(loc="lower right")
        return mo.center(fig)


    lin_sim_k3()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Controller Tuned with Pole Assignment

    Using pole assignement, find a matrix

    $$
    K_{pp} =
    \begin{bmatrix}
    ? & ? & ? & ?
    \end{bmatrix}
    \in \mathbb{R}^{4\times 1}
    $$

    such that the control law

    $$
    \Delta \phi(t)
    = - K_{pp} \cdot
    \begin{bmatrix}
    \Delta x(t) \\
    \Delta \dot{x}(t) \\
    \Delta \theta(t) \\
    \Delta \dot{\theta}(t)
    \end{bmatrix} \in \mathbb{R}
    $$

    satisfies the conditions defined for the manually tuned controller and additionally:

    - result in an asymptotically stable closed-loop dynamics,

    - make $\Delta x(t) \to 0$ in approximately $20$ sec (or less).

    Explain how you find the proper design parameters!
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### 🔓 Solution
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We decide to try to cluster all our eigenvalue near a single real (negative) value
    $s$. If we want a convergence at 5% in 20 seconds at most, we know that $|\lambda|$
    should be at least $3 / 20 = 0.15$.

    Experimentally however this is a bit slow to converge (see below), the setup is better if we pick a faster dynamics, to have our eigenvalues clustered around $-0.5$ for example.

    There is actually quite a range of locations that work, but around $-0.1$, we start compensating too fast and to violate the constraint on the maximal value of $\phi$.
    """)
    return


@app.cell
def _(A_lat, B_lat, make_fun_lat, mo, np, plt, sci, scipy):
    def lin_sim_3():
        K = scipy.signal.place_poles(
            A=A_lat,
            B=B_lat,
            poles=-0.15 * np.array([1.0, 1.01, 1.02, 1.03]),
        ).gain_matrix.squeeze()

        print(f"K = {K}")

        print(
            "eigenvalues:",
            np.linalg.eig(
                A_lat - B_lat.reshape((-1, 1)) @ K.reshape((1, -1))
            ).eigenvalues,
        )

        t_span = [0, 20.0]
        t = np.linspace(t_span[0], t_span[1], 1000)
        state_0 = [0, 0, 45 * np.pi / 180.0, 0]

        def phi(t, state):
            return -K.dot(state)

        f_lat = make_fun_lat(phi)
        r = sci.solve_ivp(fun=f_lat, y0=state_0, t_span=t_span, dense_output=True)
        sol_lin_t = r.sol(t)

        fig, (ax1, ax2, ax3) = plt.subplots(3, 1, sharex=True, figsize=(12, 6))
        ax1.plot(t, sol_lin_t[0], label=r"$x(t)$ (lin.)")
        ax1.grid(True)
        ax1.legend(loc="lower right")
        ax2.plot(t, sol_lin_t[2], label=r"$\theta(t)$ (lin.)")
        ax2.plot(t, 0.5 * np.pi * np.ones_like(t), "r--", label=r"$\pm\pi/2$")
        ax2.plot(t, -0.5 * np.pi * np.ones_like(t), "r--")
        ax2.grid(True)
        ax2.legend(loc="lower right")
        ax3.plot(t, phi(t, sol_lin_t), label=r"$\phi(t)$ (lin.)")
        ax3.grid(True)
        ax3.plot(t, 0.5 * np.pi * np.ones_like(t), "r--", label=r"$\pm\pi/2$")
        ax3.plot(t, -0.5 * np.pi * np.ones_like(t), "r--")
        ax3.set_xlabel(r"time $t$")
        ax3.legend(loc="lower right")
        return mo.center(fig)


    lin_sim_3()
    return


@app.cell
def _(A_lat, B_lat, make_fun_lat, mo, np, plt, sci, scipy):
    Kpp = scipy.signal.place_poles(
        A=A_lat,
        B=B_lat,
        poles=-0.5 * np.array([1.0, 1.01, 1.02, 1.03]),
    ).gain_matrix.squeeze()


    def lin_sim_32():
        K = Kpp
        print(f"K = {K}")

        print(
            "eigenvalues:",
            np.linalg.eig(
                A_lat - B_lat.reshape((-1, 1)) @ K.reshape((1, -1))
            ).eigenvalues,
        )

        t_span = [0, 20.0]
        t = np.linspace(t_span[0], t_span[1], 1000)
        state_0 = [0, 0, 45 * np.pi / 180.0, 0]

        def phi(t, state):
            return -K.dot(state)

        f_lat = make_fun_lat(phi)
        r = sci.solve_ivp(fun=f_lat, y0=state_0, t_span=t_span, dense_output=True)
        sol_lin_t = r.sol(t)

        fig, (ax1, ax2, ax3) = plt.subplots(3, 1, sharex=True, figsize=(12, 6))
        ax1.plot(t, sol_lin_t[0], label=r"$x(t)$ (lin.)")
        ax1.grid(True)
        ax1.legend(loc="lower right")
        ax2.plot(t, sol_lin_t[2], label=r"$\theta(t)$ (lin.)")
        ax2.plot(t, 0.5 * np.pi * np.ones_like(t), "r--", label=r"$\pm\pi/2$")
        ax2.plot(t, -0.5 * np.pi * np.ones_like(t), "r--")
        ax2.grid(True)
        ax2.legend(loc="lower right")
        ax3.plot(t, phi(t, sol_lin_t), label=r"$\phi(t)$ (lin.)")
        ax3.grid(True)
        ax3.plot(t, 0.5 * np.pi * np.ones_like(t), "r--", label=r"$\pm\pi/2$")
        ax3.plot(t, -0.5 * np.pi * np.ones_like(t), "r--")
        ax3.set_xlabel(r"time $t$")
        ax3.legend(loc="lower right")
        return mo.center(fig)


    lin_sim_32()
    return (Kpp,)


@app.cell
def _(A_lat, B_lat, make_fun_lat, mo, np, plt, sci, scipy):
    def lin_sim_33():
        K = scipy.signal.place_poles(
            A=A_lat,
            B=B_lat,
            poles=-1.0 * np.array([1.0, 1.01, 1.02, 1.03]),
        ).gain_matrix.squeeze()

        print(f"K = {K}")

        print(
            "eigenvalues:",
            np.linalg.eig(
                A_lat - B_lat.reshape((-1, 1)) @ K.reshape((1, -1))
            ).eigenvalues,
        )

        t_span = [0, 20.0]
        t = np.linspace(t_span[0], t_span[1], 1000)
        state_0 = [0, 0, 45 * np.pi / 180.0, 0]

        def phi(t, state):
            return -K.dot(state)

        f_lat = make_fun_lat(phi)
        r = sci.solve_ivp(fun=f_lat, y0=state_0, t_span=t_span, dense_output=True)
        sol_lin_t = r.sol(t)

        fig, (ax1, ax2, ax3) = plt.subplots(3, 1, sharex=True, figsize=(12, 6))
        ax1.plot(t, sol_lin_t[0], label=r"$x(t)$ (lin.)")
        ax1.grid(True)
        ax1.legend(loc="lower right")
        ax2.plot(t, sol_lin_t[2], label=r"$\theta(t)$ (lin.)")
        ax2.plot(t, 0.5 * np.pi * np.ones_like(t), "r--", label=r"$\pm\pi/2$")
        ax2.plot(t, -0.5 * np.pi * np.ones_like(t), "r--")
        ax2.grid(True)
        ax2.legend(loc="lower right")
        ax3.plot(t, phi(t, sol_lin_t), label=r"$\phi(t)$ (lin.)")
        ax3.grid(True)
        ax3.plot(t, 0.5 * np.pi * np.ones_like(t), "r--", label=r"$\pm\pi/2$")
        ax3.plot(t, -0.5 * np.pi * np.ones_like(t), "r--")
        ax3.set_xlabel(r"time $t$")
        ax3.legend(loc="lower right")
        return mo.center(fig)


    lin_sim_33()
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## 🧩 Controller Tuned with Optimal Control

    Using optimal control, find a gain matrix $K_{oc}$ that satisfies the same set of requirements that the one defined using pole placement.

    Explain how you find the proper design parameters!
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### 🔓 Solution
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The basic optimal control design, with

    $$
    Q = \begin{bmatrix}
    1 & 0 & 0 & 0 \\
    0 & 0 & 0 & 0 \\
    0 & 0 & 1 & 0 \\
    0 & 0 & 0 & 1
    \end{bmatrix},
    $$

    and

    $$
    R = \begin{bmatrix}
    1
    \end{bmatrix},
    $$
    almost makes the job, except that it is a bit too fast and that results initially in large values of the angle $\phi$.
    """)
    return


@app.cell
def _(A_lat, B_lat, make_fun_lat, mo, np, plt, sci, scipy):
    def lin_sim_4():
        Q = np.eye(4,4)
        print("Q:", Q)
        R = np.eye(1) #10*l**2 * np.eye(1)
        print("R:", R)
        Pi = scipy.linalg.solve_continuous_are(
            a=A_lat, 
            b=B_lat, 
            q=Q, 
            r=R
        )
        Koc = (np.linalg.inv(R) @ B_lat.T @ Pi).squeeze()

        K = Koc
        print(f"K = {K}")

        print(
            "eigenvalues:",
            np.linalg.eig(
                A_lat - B_lat.reshape((-1, 1)) @ K.reshape((1, -1))
            ).eigenvalues,
        )

        t_span = [0, 20.0]
        t = np.linspace(t_span[0], t_span[1], 1000)
        state_0 = [0, 0, 45 * np.pi / 180.0, 0]

        def phi(t, state):
            return -K.dot(state)

        f_lat = make_fun_lat(phi)
        r = sci.solve_ivp(fun=f_lat, y0=state_0, t_span=t_span, dense_output=True)
        sol_lin_t = r.sol(t)

        fig, (ax1, ax2, ax3) = plt.subplots(3, 1, sharex=True, figsize=(12, 6))
        ax1.plot(t, sol_lin_t[0], label=r"$x(t)$ (lin.)")
        ax1.grid(True)
        ax1.legend(loc="lower right")
        ax2.plot(t, sol_lin_t[2], label=r"$\theta(t)$ (lin.)")
        ax2.plot(t, 0.5 * np.pi * np.ones_like(t), "r--", label=r"$\pm\pi/2$")
        ax2.plot(t, -0.5 * np.pi * np.ones_like(t), "r--")
        ax2.grid(True)
        ax2.legend(loc="lower right")
        ax3.plot(t, phi(t, sol_lin_t), label=r"$\phi(t)$ (lin.)")
        ax3.grid(True)
        ax3.plot(t, 0.5 * np.pi * np.ones_like(t), "r--", label=r"$\pm\pi/2$")
        ax3.plot(t, -0.5 * np.pi * np.ones_like(t), "r--")
        ax3.set_xlabel(r"time $t$")
        ax3.legend(loc="lower right")
        return mo.center(fig)


    lin_sim_4()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    A second design with the same $Q$ but $R$ increased by $100$ (to reduce the activation of the input at the price of some convergence speed) performs adequately!
    """)
    return


@app.cell
def _(A_lat, B_lat, make_fun_lat, mo, np, plt, sci, scipy):
    Q = np.eye(4,4)
    print("Q:", Q)
    R = 100 * np.eye(1)
    print("R:", R)
    Pi = scipy.linalg.solve_continuous_are(
        a=A_lat, 
        b=B_lat, 
        q=Q, 
        r=R
    )
    Koc = (np.linalg.inv(R) @ B_lat.T @ Pi).squeeze()

    def lin_sim_42():
        K = Koc
        print(f"K = {K}")

        print(
            "eigenvalues:",
            np.linalg.eig(
                A_lat - B_lat.reshape((-1, 1)) @ K.reshape((1, -1))
            ).eigenvalues,
        )

        t_span = [0, 20.0]
        t = np.linspace(t_span[0], t_span[1], 1000)
        state_0 = [0, 0, 45 * np.pi / 180.0, 0]

        def phi(t, state):
            return -K.dot(state)

        f_lat = make_fun_lat(phi)
        r = sci.solve_ivp(fun=f_lat, y0=state_0, t_span=t_span, dense_output=True)
        sol_lin_t = r.sol(t)

        fig, (ax1, ax2, ax3) = plt.subplots(3, 1, sharex=True, figsize=(12, 6))
        ax1.plot(t, sol_lin_t[0], label=r"$x(t)$ (lin.)")
        ax1.grid(True)
        ax1.legend(loc="lower right")
        ax2.plot(t, sol_lin_t[2], label=r"$\theta(t)$ (lin.)")
        ax2.plot(t, 0.5 * np.pi * np.ones_like(t), "r--", label=r"$\pm\pi/2$")
        ax2.plot(t, -0.5 * np.pi * np.ones_like(t), "r--")
        ax2.grid(True)
        ax2.legend(loc="lower right")
        ax3.plot(t, phi(t, sol_lin_t), label=r"$\phi(t)$ (lin.)")
        ax3.grid(True)
        ax3.plot(t, 0.5 * np.pi * np.ones_like(t), "r--", label=r"$\pm\pi/2$")
        ax3.plot(t, -0.5 * np.pi * np.ones_like(t), "r--")
        ax3.set_xlabel(r"time $t$")
        ax3.legend(loc="lower right")
        return mo.center(fig)


    lin_sim_42()
    return (Koc,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Validation

    Test the two control strategies (pole placement and optimal control) on the "true" (nonlinear) model with an animation. Check that both controllers achieve their goal; otherwise, go back to the drawing board and tweak the design parameters until they do!
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### 🔓 Solution
    """)
    return


@app.cell(hide_code=True)
def _(Kpp, M, booster_anim, g, mo, np, redstart_solve, world):
    def _anim():
        t_span = [0.0, 20.0]
        y0 = [0.0, 0.0, 20.0, 0.0, 45 * np.pi/180.0, 0.0]
        def f_phi(t, state):
            x, dx, y, dy, theta, dtheta = state  
            return np.array(
                [M*g, -Kpp.dot([x, dx, theta, dtheta])]
            )
        sol = redstart_solve(t_span, y0, f_phi)
        x = lambda t: sol(t)[0]
        y = lambda t: sol(t)[2]
        theta = lambda t : sol(t)[4]
        f = lambda t: f_phi(t, sol(t))[0]
        phi = lambda t: f_phi(t, sol(t))[1]
        return mo.Html(
            world(
                [-6, 6, -2, 22], 
                booster_anim(x, y, theta, f, phi, T=t_span[1])
            )
        ).center()

    _anim()
    return


@app.cell(hide_code=True)
def _(Koc, M, booster_anim, g, mo, np, redstart_solve, world):
    def _anim():
        t_span = [0.0, 20.0]
        y0 = [0.0, 0.0, 20.0, 0.0, 45 * np.pi/180.0, 0.0]
        def f_phi(t, state):
            x, dx, y, dy, theta, dtheta = state  
            return np.array(
                [M*g, -Koc.dot([x, dx, theta, dtheta])]
            )
        sol = redstart_solve(t_span, y0, f_phi)
        x = lambda t: sol(t)[0]
        y = lambda t: sol(t)[2]
        theta = lambda t : sol(t)[4]
        f = lambda t: f_phi(t, sol(t))[0]
        phi = lambda t: f_phi(t, sol(t))[1]
        return mo.Html(
            world(
                [-6, 6, -2, 22], 
                booster_anim(x, y, theta, f, phi, T=t_span[1])
            )
        ).center()

    _anim()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Exact Linearization

    Let
    $$
    R(\alpha) =
    \begin{bmatrix} +\cos \alpha & -\sin \alpha \\ +\sin \alpha & -\cos \alpha
    \end{bmatrix}
    $$

    Consider an auxiliary system which is meant to compute the force $(f_x, f_y)$ applied to the booster.

    The inputs of the auxiliary system are

    $$
    v = (v_1, v_2) \in \mathbb{R}^2,
    $$

    its dynamics

    $$
    \ddot{z} = v_1 \qquad \text{ where } \qquad z \in \mathbb{R}
    $$

    and its output $(f_x, f_y) \in \mathbb{R}^2$ is given by

    \[
    \begin{bmatrix}
    f_x \\
    f_y
    \end{bmatrix} = R\left(\theta - \frac{\pi}{2}\right)
    \begin{bmatrix}
    z - M\ell\dot{\theta}^2 / 6 \\
    {M\ell v_2}/{6z}
    \end{bmatrix}
    \]

    ⚠️ Note that the second component $f_y$ of the reactor force is undefined whenever $z=0$.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Geometrical Interpretation


    Consider the output $h$ of the original system

    $$
    h :=
    \begin{bmatrix}
    x - (\ell/6) \sin \theta \\
    y + (\ell/6) \cos \theta
    \end{bmatrix} \in \mathbb{R}^2
    $$

    Provide a geometrical interpretation of $h$ (for example, make a drawing).
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    On définit
    \[
    h =
    \begin{bmatrix}
    x-\frac{\ell}{6}\sin\theta\\
    y+\frac{\ell}{6}\cos\theta
    \end{bmatrix}.
    \]

    Le vecteur unitaire dirigé le long du booster, du centre de masse vers le haut du booster, est
    \[
    \begin{bmatrix}
    -\sin\theta\\
    \cos\theta
    \end{bmatrix}.
    \]

    Ainsi,
    \[
    h =
    \begin{bmatrix}
    x\\
    y
    \end{bmatrix}
    +
    \frac{\ell}{6}
    \begin{bmatrix}
    -\sin\theta\\
    \cos\theta
    \end{bmatrix}.
    \]

    Donc \(h\) représente un point situé sur l’axe du booster, à une distance \(\ell/6\) au-dessus du centre de masse. Ce n’est pas le sommet du booster, qui serait à une distance \(\ell/2\), mais un point interne du corps.
    """)
    return


@app.cell
def _(np, plt):


    def draw_booster(ax, theta=0, title=""):
        # Paramètres géométriques
        L = 2.0  # Longueur totale du booster
        l_h = L/6 # Position de h par rapport au CM (selon ton code)
    
        # Coordonnées du centre de masse (CM)
        x_cm, y_cm = 0, 0
    
        # Calcul des positions
        # On utilise sin/cos selon la convention : theta=0 est vertical
        top = np.array([x_cm - (L/2)*np.sin(theta), y_cm + (L/2)*np.cos(theta)])
        bot = np.array([x_cm + (L/2)*np.sin(theta), y_cm - (L/2)*np.cos(theta)])
        h_pt = np.array([x_cm - l_h*np.sin(theta), y_cm + l_h*np.cos(theta)])
    
        # 1. Dessin du corps du booster (Ligne épaisse grise)
        ax.plot([bot[0], top[0]], [bot[1], top[1]], color='#2c3e50', lw=6, solid_capstyle='round', label="Corps")
    
        # 2. Dessin du réacteur (un triangle rouge à la base)
        ax.plot(bot[0], bot[1], 'r^', ms=12, label="Réacteur")
    
        # 3. Dessin de la flamme (si incliné, pour le style)
        if abs(theta) > 0.01:
            flame_end = bot + 0.3 * np.array([np.sin(theta), -np.cos(theta)])
            ax.plot([bot[0], flame_end[0]], [bot[1], flame_end[1]], color='orange', lw=3, ls='--')

        # 4. Points clés
        ax.plot(x_cm, y_cm, 'bo', ms=8, label="CM (G)")
        ax.plot(h_pt[0], h_pt[1], 'rs', ms=10, label=r"Point $h$ (Sortie Plate)")
    
        # 5. Ligne de référence verticale (pointillés)
        ax.axvline(0, color='black', ls=':', alpha=0.3)
    
        # Esthétique du graphe
        ax.set_aspect('equal')
        ax.grid(True, linestyle='--', alpha=0.6)
        ax.set_title(title, fontsize=12, fontweight='bold')
        ax.set_xlim(-1.5, 1.5)
        ax.set_ylim(-1.5, 1.5)
        ax.legend(prop={'size': 8}, loc='upper right')

    # Génération des deux graphiques
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 7))

    # Cas 1 : Vertical (theta = 0)
    draw_booster(ax1, theta=0, title="Configuration Verticale\n($\\theta = 0$)")

    # Cas 2 : Incliné (theta = 30 degrés)
    theta_rad = np.radians(30)
    draw_booster(ax2, theta=theta_rad, title="Configuration Inclinée\n($\\theta = 30^\\circ$)")

    plt.tight_layout()
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 First and Second-Order Derivatives

    Compute $\dot{h}$ as a function of $\dot{x}$, $\dot{y}$, $\theta$ and $\dot{\theta}$ (and constants) and then $\ddot{h}$ as a function of $\theta$ and $z$ (and constants) when the auxiliary system is plugged in the booster.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    On part de la définition
    \[
    h_x=x-\frac{\ell}{6}\sin\theta,
    \qquad
    h_y=y+\frac{\ell}{6}\cos\theta.
    \]

    On dérive d’abord \(h_x\). Comme
    \[
    \frac{d}{dt}\sin\theta=\cos\theta\,\dot\theta,
    \]
    on obtient
    \[
    \dot h_x
    =
    \dot x-\frac{\ell}{6}\cos\theta\,\dot\theta.
    \]

    De même, comme
    \[
    \frac{d}{dt}\cos\theta=-\sin\theta\,\dot\theta,
    \]
    on obtient
    \[
    \dot h_y
    =
    \dot y-\frac{\ell}{6}\sin\theta\,\dot\theta.
    \]

    Ainsi,
    \[
    \boxed{
    \dot h
    =
    \begin{pmatrix}
    \dot x-\frac{\ell}{6}\cos\theta\,\dot\theta\\
    \dot y-\frac{\ell}{6}\sin\theta\,\dot\theta
    \end{pmatrix}.
    }
    \]

    On dérive maintenant une deuxième fois.

    Pour \(h_x\),
    \[
    \dot h_x
    =
    \dot x-\frac{\ell}{6}\cos\theta\,\dot\theta.
    \]

    Donc
    \[
    \ddot h_x
    =
    \ddot x
    -\frac{\ell}{6}
    \frac{d}{dt}
    \left(
    \cos\theta\,\dot\theta
    \right).
    \]

    Or
    \[
    \frac{d}{dt}
    \left(
    \cos\theta\,\dot\theta
    \right)
    =
    -\sin\theta\,\dot\theta^2
    +
    \cos\theta\,\ddot\theta.
    \]

    Donc
    \[
    \ddot h_x
    =
    \ddot x
    +\frac{\ell}{6}\sin\theta\,\dot\theta^2
    -\frac{\ell}{6}\cos\theta\,\ddot\theta.
    \]

    Pour \(h_y\),
    \[
    \dot h_y
    =
    \dot y-\frac{\ell}{6}\sin\theta\,\dot\theta.
    \]

    Donc
    \[
    \ddot h_y
    =
    \ddot y
    -\frac{\ell}{6}
    \frac{d}{dt}
    \left(
    \sin\theta\,\dot\theta
    \right).
    \]

    Or
    \[
    \frac{d}{dt}
    \left(
    \sin\theta\,\dot\theta
    \right)
    =
    \cos\theta\,\dot\theta^2
    +
    \sin\theta\,\ddot\theta.
    \]

    Donc
    \[
    \ddot h_y
    =
    \ddot y
    -\frac{\ell}{6}\cos\theta\,\dot\theta^2
    -\frac{\ell}{6}\sin\theta\,\ddot\theta.
    \]

    On a donc
    \[
    \boxed{
    \ddot h_x
    =
    \ddot x
    +\frac{\ell}{6}\sin\theta\,\dot\theta^2
    -\frac{\ell}{6}\cos\theta\,\ddot\theta,
    }
    \]
    et
    \[
    \boxed{
    \ddot h_y
    =
    \ddot y
    -\frac{\ell}{6}\cos\theta\,\dot\theta^2
    -\frac{\ell}{6}\sin\theta\,\ddot\theta.
    }
    \]

    On injecte maintenant la dynamique.

    Le système auxiliaire donne
    \[
    \begin{pmatrix}
    f_x\\
    f_y
    \end{pmatrix}
    =
    R\left(\theta-\frac{\pi}{2}\right)
    \begin{pmatrix}
    z-\frac{M\ell\dot\theta^2}{6}\\
    \frac{M\ell v_2}{6z}
    \end{pmatrix}.
    \]

    D’après l’expression donnée,
    \[
    R\left(\theta-\frac{\pi}{2}\right)
    =
    \begin{pmatrix}
    \sin\theta & \cos\theta\\
    -\cos\theta & \sin\theta
    \end{pmatrix}.
    \]

    Donc
    \[
    f_x
    =
    \sin\theta
    \left(
    z-\frac{M\ell\dot\theta^2}{6}
    \right)
    +
    \cos\theta
    \left(
    \frac{M\ell v_2}{6z}
    \right),
    \]
    et
    \[
    f_y
    =
    -\cos\theta
    \left(
    z-\frac{M\ell\dot\theta^2}{6}
    \right)
    +
    \sin\theta
    \left(
    \frac{M\ell v_2}{6z}
    \right).
    \]

    La dynamique de translation est
    \[
    M\ddot x=f_x,
    \qquad
    M\ddot y=f_y-Mg.
    \]

    Donc
    \[
    \ddot x
    =
    \frac{z}{M}\sin\theta
    -\frac{\ell}{6}\dot\theta^2\sin\theta
    +\frac{\ell v_2}{6z}\cos\theta,
    \]
    et
    \[
    \ddot y
    =
    -\frac{z}{M}\cos\theta
    +\frac{\ell}{6}\dot\theta^2\cos\theta
    +\frac{\ell v_2}{6z}\sin\theta
    -g.
    \]

    La dynamique angulaire donne, avec la construction auxiliaire,
    \[
    \ddot\theta=\frac{v_2}{z}.
    \]

    On remplace maintenant dans \(\ddot h_x\) :
    \[
    \ddot h_x
    =
    \left(
    \frac{z}{M}\sin\theta
    -\frac{\ell}{6}\dot\theta^2\sin\theta
    +\frac{\ell v_2}{6z}\cos\theta
    \right)
    +
    \frac{\ell}{6}\sin\theta\,\dot\theta^2
    -
    \frac{\ell}{6}\cos\theta
    \left(
    \frac{v_2}{z}
    \right).
    \]

    Les termes en \(\dot\theta^2\) s’annulent :
    \[
    -\frac{\ell}{6}\dot\theta^2\sin\theta
    +
    \frac{\ell}{6}\sin\theta\,\dot\theta^2
    =0.
    \]

    Les termes en \(v_2\) s’annulent aussi :
    \[
    \frac{\ell v_2}{6z}\cos\theta
    -
    \frac{\ell}{6}\cos\theta\frac{v_2}{z}
    =0.
    \]

    Il reste donc
    \[
    \boxed{
    \ddot h_x=\frac{z}{M}\sin\theta.
    }
    \]

    De même, pour \(\ddot h_y\),
    \[
    \ddot h_y
    =
    \left(
    -\frac{z}{M}\cos\theta
    +\frac{\ell}{6}\dot\theta^2\cos\theta
    +\frac{\ell v_2}{6z}\sin\theta
    -g
    \right)
    -
    \frac{\ell}{6}\cos\theta\,\dot\theta^2
    -
    \frac{\ell}{6}\sin\theta
    \left(
    \frac{v_2}{z}
    \right).
    \]

    Les termes en \(\dot\theta^2\) s’annulent :
    \[
    \frac{\ell}{6}\dot\theta^2\cos\theta
    -
    \frac{\ell}{6}\cos\theta\,\dot\theta^2
    =0.
    \]

    Les termes en \(v_2\) s’annulent aussi :
    \[
    \frac{\ell v_2}{6z}\sin\theta
    -
    \frac{\ell}{6}\sin\theta\frac{v_2}{z}
    =0.
    \]

    Il reste donc
    \[
    \boxed{
    \ddot h_y=-\frac{z}{M}\cos\theta-g.
    }
    \]

    Finalement,
    \[
    \boxed{
    \ddot h
    =
    \frac{z}{M}
    \begin{pmatrix}
    \sin\theta\\
    -\cos\theta
    \end{pmatrix}
    -
    \begin{pmatrix}
    0\\
    g
    \end{pmatrix}.
    }
    \]

    Le point important est que le choix de \(h\) à distance \(\ell/6\) du centre de masse fait disparaître les termes en \(\dot\theta^2\) et en \(v_2\). C’est cette annulation qui prépare la linéarisation exacte.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Third and Fourth-Order Derivatives

    Compute the third derivative $h^{(3)}$ of $h$ as a function of $\theta$ and $z$ (and constants) and then the fourth derivative $h^{(4)}$ of $h$ with respect to time as a function of $\theta$, $\dot{\theta}$, $z$, $\dot{z}$, $v$ (and constants) when the auxiliary system is on.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    On a obtenu
    \[
    \ddot h
    =
    -\begin{pmatrix}
    0\\
    g
    \end{pmatrix}
    +
    \frac{z}{M}
    \begin{pmatrix}
    \sin\theta\\
    -\cos\theta
    \end{pmatrix}.
    \]

    Pour simplifier les notations, on pose
    \[
    e(\theta)
    =
    \begin{pmatrix}
    \sin\theta\\
    -\cos\theta
    \end{pmatrix}.
    \]

    On introduit aussi
    \[
    n(\theta)
    =
    \begin{pmatrix}
    \cos\theta\\
    \sin\theta
    \end{pmatrix}.
    \]

    On remarque que
    \[
    \dot e(\theta)
    =
    \dot\theta
    \begin{pmatrix}
    \cos\theta\\
    \sin\theta
    \end{pmatrix}
    =
    \dot\theta\, n(\theta).
    \]

    Donc
    \[
    \ddot h
    =
    -\begin{pmatrix}
    0\\
    g
    \end{pmatrix}
    +
    \frac{z}{M}e(\theta).
    \]

    La dérivée du terme constant est nulle. Ainsi,
    \[
    h^{(3)}
    =
    \frac{d}{dt}
    \left(
    \frac{z}{M}e(\theta)
    \right).
    \]

    On utilise la règle du produit :
    \[
    h^{(3)}
    =
    \frac{\dot z}{M}e(\theta)
    +
    \frac{z}{M}\dot e(\theta).
    \]

    Comme
    \[
    \dot e(\theta)=\dot\theta\,n(\theta),
    \]
    on obtient
    \[
    \boxed{
    h^{(3)}
    =
    \frac{\dot z}{M}e(\theta)
    +
    \frac{z\dot\theta}{M}n(\theta).
    }
    \]

    On dérive encore pour obtenir \(h^{(4)}\).

    On part de
    \[
    h^{(3)}
    =
    \frac{\dot z}{M}e(\theta)
    +
    \frac{z\dot\theta}{M}n(\theta).
    \]

    On dérive le premier terme :
    \[
    \frac{d}{dt}
    \left(
    \frac{\dot z}{M}e(\theta)
    \right)
    =
    \frac{\ddot z}{M}e(\theta)
    +
    \frac{\dot z}{M}\dot e(\theta).
    \]

    Or
    \[
    \dot e(\theta)=\dot\theta n(\theta).
    \]

    Donc
    \[
    \frac{d}{dt}
    \left(
    \frac{\dot z}{M}e(\theta)
    \right)
    =
    \frac{\ddot z}{M}e(\theta)
    +
    \frac{\dot z\dot\theta}{M}n(\theta).
    \]

    On dérive maintenant le second terme :
    \[
    \frac{d}{dt}
    \left(
    \frac{z\dot\theta}{M}n(\theta)
    \right)
    =
    \frac{\dot z\dot\theta+z\ddot\theta}{M}n(\theta)
    +
    \frac{z\dot\theta}{M}\dot n(\theta).
    \]

    Or
    \[
    n(\theta)
    =
    \begin{pmatrix}
    \cos\theta\\
    \sin\theta
    \end{pmatrix},
    \]
    donc
    \[
    \dot n(\theta)
    =
    \dot\theta
    \begin{pmatrix}
    -\sin\theta\\
    \cos\theta
    \end{pmatrix}
    =
    -\dot\theta
    \begin{pmatrix}
    \sin\theta\\
    -\cos\theta
    \end{pmatrix}
    =
    -\dot\theta e(\theta).
    \]

    Ainsi,
    \[
    \frac{d}{dt}
    \left(
    \frac{z\dot\theta}{M}n(\theta)
    \right)
    =
    \frac{\dot z\dot\theta+z\ddot\theta}{M}n(\theta)
    -
    \frac{z\dot\theta^2}{M}e(\theta).
    \]

    En regroupant les termes selon \(e(\theta)\) et \(n(\theta)\), on obtient
    \[
    h^{(4)}
    =
    \left(
    \frac{\ddot z}{M}
    -
    \frac{z\dot\theta^2}{M}
    \right)e(\theta)
    +
    \left(
    \frac{\dot z\dot\theta}{M}
    +
    \frac{\dot z\dot\theta+z\ddot\theta}{M}
    \right)n(\theta).
    \]

    Donc
    \[
    h^{(4)}
    =
    \frac{\ddot z-z\dot\theta^2}{M}e(\theta)
    +
    \frac{2\dot z\dot\theta+z\ddot\theta}{M}n(\theta).
    \]

    Le système auxiliaire donne
    \[
    \ddot z=v_1,
    \qquad
    z\ddot\theta=v_2.
    \]

    En remplaçant,
    \[
    \boxed{
    h^{(4)}
    =
    \frac{v_1-z\dot\theta^2}{M}e(\theta)
    +
    \frac{2\dot z\dot\theta+v_2}{M}n(\theta).
    }
    \]

    Cette expression est essentielle : les entrées \(v_1\) et \(v_2\) apparaissent linéairement dans la quatrième dérivée de \(h\).
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Exact Linearization

    Show that with yet another auxiliary system with input $u=(u_1, u_2)$ and output $v$ fed into the previous one, we can achieve the dynamics

    $$
    h^{(4)} = u
    $$
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    On veut imposer une dynamique simple :
    \[
    h^{(4)}=u,
    \qquad
    u=
    \begin{pmatrix}
    u_1\\
    u_2
    \end{pmatrix}.
    \]

    On a montré que
    \[
    h^{(4)}
    =
    \frac{v_1-z\dot\theta^2}{M}e(\theta)
    +
    \frac{2\dot z\dot\theta+v_2}{M}n(\theta),
    \]
    où
    \[
    e(\theta)
    =
    \begin{pmatrix}
    \sin\theta\\
    -\cos\theta
    \end{pmatrix},
    \qquad
    n(\theta)
    =
    \begin{pmatrix}
    \cos\theta\\
    \sin\theta
    \end{pmatrix}.
    \]

    Les deux vecteurs \(e(\theta)\) et \(n(\theta)\) sont orthonormés. En effet,
    \[
    \|e(\theta)\|^2
    =
    \sin^2\theta+\cos^2\theta=1,
    \]
    \[
    \|n(\theta)\|^2
    =
    \cos^2\theta+\sin^2\theta=1,
    \]
    et
    \[
    e(\theta)^\top n(\theta)
    =
    \sin\theta\cos\theta-\cos\theta\sin\theta=0.
    \]

    Donc tout vecteur \(u\in\mathbb{R}^2\) se décompose dans cette base :
    \[
    u
    =
    \left(e(\theta)^\top u\right)e(\theta)
    +
    \left(n(\theta)^\top u\right)n(\theta).
    \]

    Pour obtenir \(h^{(4)}=u\), on identifie les coefficients devant \(e(\theta)\) et \(n(\theta)\).

    On veut
    \[
    \frac{v_1-z\dot\theta^2}{M}
    =
    e(\theta)^\top u.
    \]

    Donc
    \[
    v_1-z\dot\theta^2
    =
    M e(\theta)^\top u,
    \]
    et finalement
    \[
    \boxed{
    v_1
    =
    M e(\theta)^\top u
    +
    z\dot\theta^2.
    }
    \]

    De même, on veut
    \[
    \frac{2\dot z\dot\theta+v_2}{M}
    =
    n(\theta)^\top u.
    \]

    Donc
    \[
    2\dot z\dot\theta+v_2
    =
    M n(\theta)^\top u,
    \]
    et
    \[
    \boxed{
    v_2
    =
    M n(\theta)^\top u
    -
    2\dot z\dot\theta.
    }
    \]

    Avec ce choix des entrées auxiliaires, on obtient exactement
    \[
    \boxed{
    h^{(4)}=u.
    }
    \]

    Le système non linéaire initial est donc transformé, en entrée-sortie, en deux intégrateurs d’ordre quatre indépendants.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 State to Derivatives of the Output

    Implement a function `Tr` of `x, dx, y, dy, theta, dtheta, z, dz` that returns `h_x, h_y, dh_x, dh_y, d2h_x, d2h_y, d3h_x, d3h_y`.
    """)
    return


@app.cell
def _(M, g, l, np):
    def Tr(x, dx, y, dy, theta, dtheta, z, dz):
        s = np.sin(theta)
        c = np.cos(theta)

        e = np.array([s, -c])
        n = np.array([c, s])

        h = np.array([
            x - (l / 6) * s,
            y + (l / 6) * c,
        ])

        dh = np.array([
            dx - (l / 6) * c * dtheta,
            dy - (l / 6) * s * dtheta,
        ])

        d2h = (z / M) * e - np.array([0.0, g])

        d3h = (dz / M) * e + (z * dtheta / M) * n

        return np.array([
            h[0], h[1],
            dh[0], dh[1],
            d2h[0], d2h[1],
            d3h[0], d3h[1],
        ])

    return (Tr,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Inversion


    Assume for the sake of simplicity that $z<0$ at all times. Show that given the values of $h$, $\dot{h}$, $\ddot{h}$ and $h^{(3)}$, one can uniquely compute the booster state (the values of $x$, $\dot{x}$, $y$, $\dot{y}$, $\theta$, $\dot{\theta}$) and auxiliary system state (the values of $z$ and $\dot{z}$).

    Implement the corresponding function `T_inv`.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    -------------------------

    On suppose que
    \[
    z<0.
    \]

    On veut retrouver
    \[
    x,\dot x,y,\dot y,\theta,\dot\theta,z,\dot z
    \]
    à partir de
    \[
    h,\dot h,\ddot h,h^{(3)}.
    \]

    On part de la relation
    \[
    \ddot h
    =
    \frac{z}{M}e(\theta)
    -
    \begin{pmatrix}
    0\\
    g
    \end{pmatrix}.
    \]

    Donc
    \[
    \ddot h+
    \begin{pmatrix}
    0\\
    g
    \end{pmatrix}
    =
    \frac{z}{M}e(\theta).
    \]

    Comme \(e(\theta)\) est unitaire, on a
    \[
    \left\|
    \ddot h+
    \begin{pmatrix}
    0\\
    g
    \end{pmatrix}
    \right\|
    =
    \left|
    \frac{z}{M}
    \right|.
    \]

    Comme \(M>0\) et que l’on suppose \(z<0\), on obtient
    \[
    \boxed{
    z
    =
    -M
    \left\|
    \ddot h+
    \begin{pmatrix}
    0\\
    g
    \end{pmatrix}
    \right\|.
    }
    \]

    Une fois \(z\) connu,
    \[
    e(\theta)
    =
    \frac{M}{z}
    \left(
    \ddot h+
    \begin{pmatrix}
    0\\
    g
    \end{pmatrix}
    \right).
    \]

    Or
    \[
    e(\theta)
    =
    \begin{pmatrix}
    \sin\theta\\
    -\cos\theta
    \end{pmatrix}.
    \]

    Donc si
    \[
    e(\theta)=
    \begin{pmatrix}
    e_1\\
    e_2
    \end{pmatrix},
    \]
    alors
    \[
    \sin\theta=e_1,
    \qquad
    \cos\theta=-e_2.
    \]

    On récupère donc
    \[
    \boxed{
    \theta=\operatorname{arg}(e_2 - i.e_1).
    }
    \]

    Ensuite, on utilise
    \[
    h^{(3)}
    =
    \frac{\dot z}{M}e(\theta)
    +
    \frac{z\dot\theta}{M}n(\theta).
    \]

    On projette d’abord sur \(e(\theta)\). Comme \(e^\top n=0\) et \(e^\top e=1\),
    \[
    e^\top h^{(3)}
    =
    \frac{\dot z}{M}.
    \]

    Donc
    \[
    \boxed{
    \dot z=M e(\theta)^\top h^{(3)}.
    }
    \]

    On projette ensuite sur \(n(\theta)\). Comme \(n^\top e=0\) et \(n^\top n=1\),
    \[
    n^\top h^{(3)}
    =
    \frac{z\dot\theta}{M}.
    \]

    Donc
    \[
    \boxed{
    \dot\theta=
    \frac{M}{z}n(\theta)^\top h^{(3)}.
    }
    \]

    Il reste à retrouver \(x,y,\dot x,\dot y\).

    À partir de
    \[
    h_x=x-\frac{\ell}{6}\sin\theta,
    \]
    on obtient
    \[
    \boxed{
    x=h_x+\frac{\ell}{6}\sin\theta.
    }
    \]

    À partir de
    \[
    h_y=y+\frac{\ell}{6}\cos\theta,
    \]
    on obtient
    \[
    \boxed{
    y=h_y-\frac{\ell}{6}\cos\theta.
    }
    \]

    Enfin,
    \[
    \dot h_x
    =
    \dot x-\frac{\ell}{6}\cos\theta\,\dot\theta,
    \]
    donc
    \[
    \boxed{
    \dot x=\dot h_x+\frac{\ell}{6}\cos\theta\,\dot\theta.
    }
    \]

    Et
    \[
    \dot h_y
    =
    \dot y-\frac{\ell}{6}\sin\theta\,\dot\theta,
    \]
    donc
    \[
    \boxed{
    \dot y=\dot h_y+\frac{\ell}{6}\sin\theta\,\dot\theta.
    }
    \]

    On a donc bien une inversion unique tant que \(z<0\).
    """)
    return


@app.cell
def _(M, g, l, np):
    def T_inv(h_x, h_y, dh_x, dh_y, d2h_x, d2h_y, d3h_x, d3h_y):
        shifted_d2h = np.array([d2h_x, d2h_y + g])
        norm_shifted = np.linalg.norm(shifted_d2h)

        if norm_shifted <= 1e-12:
            raise ValueError("Singularité : z est trop proche de 0.")

        z = -M * norm_shifted

        e = (M / z) * shifted_d2h
        theta = np.arctan2(e[0], -e[1])

        s = np.sin(theta)
        c = np.cos(theta)

        n = np.array([c, s])
        d3h = np.array([d3h_x, d3h_y])

        dz = M * np.dot(e, d3h)
        dtheta = (M / z) * np.dot(n, d3h)

        x = h_x + (l / 6) * s
        y = h_y - (l / 6) * c

        dx = dh_x + (l / 6) * c * dtheta
        dy = dh_y + (l / 6) * s * dtheta

        return np.array([x, dx, y, dy, theta, dtheta, z, dz])

    return (T_inv,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Admissible Path Computation

    Implement a function

    ```python
    def compute(
        x_0,
        dx_0,
        y_0,
        dy_0,
        theta_0,
        dtheta_0,
        z_0,
        dz_0,
        x_tf,
        dx_tf,
        y_tf,
        dy_tf,
        theta_tf,
        dtheta_tf,
        z_tf,
        dz_tf,
        tf,
    ):
        ...

    ```

    that returns a function `fun` such that `fun(t)` is a value of `x, dx, y, dy, theta, dtheta, z, dz, f, phi` at time `t` that match the initial and final values provided as arguments to `compute`.
    """)
    return


@app.cell
def _(M, T_inv, Tr, l, np):
    def compute(
        x_0,
        dx_0,
        y_0,
        dy_0,
        theta_0,
        dtheta_0,
        z_0,
        dz_0,
        x_tf,
        dx_tf,
        y_tf,
        dy_tf,
        theta_tf,
        dtheta_tf,
        z_tf,
        dz_tf,
        tf,
    ):
        import math

        def poly7_coeffs(initial_values, final_values, tf):
            A_mat = np.zeros((8, 8))
            b_vec = np.zeros(8)

            for k in range(4):
                A_mat[k, k] = math.factorial(k)
                b_vec[k] = initial_values[k]

            for k in range(4):
                row = 4 + k
                for i in range(k, 8):
                    A_mat[row, i] = (
                        math.factorial(i)
                        / math.factorial(i - k)
                        * tf ** (i - k)
                    )
                b_vec[row] = final_values[k]

            return np.linalg.solve(A_mat, b_vec)

        def poly_eval(coeffs, t, order):
            value = 0.0
            for i in range(order, len(coeffs)):
                value += (
                    coeffs[i]
                    * math.factorial(i)
                    / math.factorial(i - order)
                    * t ** (i - order)
                )
            return value

        def force_to_f_phi(fx, fy, theta):
            f = np.sqrt(fx ** 2 + fy ** 2)

            if f <= 1e-12:
                return 0.0, 0.0

            angle = np.arctan2(-fx, fy)
            phi = angle - theta
            phi = (phi + np.pi) % (2 * np.pi) - np.pi

            return f, phi

        Tr_0 = Tr(x_0, dx_0, y_0, dy_0, theta_0, dtheta_0, z_0, dz_0)
        Tr_tf = Tr(x_tf, dx_tf, y_tf, dy_tf, theta_tf, dtheta_tf, z_tf, dz_tf)

        coeffs_hx = poly7_coeffs(
            [Tr_0[0], Tr_0[2], Tr_0[4], Tr_0[6]],
            [Tr_tf[0], Tr_tf[2], Tr_tf[4], Tr_tf[6]],
            tf,
        )

        coeffs_hy = poly7_coeffs(
            [Tr_0[1], Tr_0[3], Tr_0[5], Tr_0[7]],
            [Tr_tf[1], Tr_tf[3], Tr_tf[5], Tr_tf[7]],
            tf,
        )

        def fun(t):
            h_x = poly_eval(coeffs_hx, t, 0)
            h_y = poly_eval(coeffs_hy, t, 0)

            dh_x = poly_eval(coeffs_hx, t, 1)
            dh_y = poly_eval(coeffs_hy, t, 1)

            d2h_x = poly_eval(coeffs_hx, t, 2)
            d2h_y = poly_eval(coeffs_hy, t, 2)

            d3h_x = poly_eval(coeffs_hx, t, 3)
            d3h_y = poly_eval(coeffs_hy, t, 3)

            d4h_x = poly_eval(coeffs_hx, t, 4)
            d4h_y = poly_eval(coeffs_hy, t, 4)

            x, dx, y, dy, theta, dtheta, z, dz = T_inv(
                h_x,
                h_y,
                dh_x,
                dh_y,
                d2h_x,
                d2h_y,
                d3h_x,
                d3h_y,
            )

            s = np.sin(theta)
            c = np.cos(theta)

            e = np.array([s, -c])
            n = np.array([c, s])

            u = np.array([d4h_x, d4h_y])

            v2 = M * np.dot(n, u) - 2 * dz * dtheta

            q1 = z - M * l * dtheta ** 2 / 6
            q2 = M * l * v2 / (6 * z)

            fx = s * q1 + c * q2
            fy = -c * q1 + s * q2

            f, phi = force_to_f_phi(fx, fy, theta)

            return np.array([x, dx, y, dy, theta, dtheta, z, dz, f, phi])

        return fun

    return (compute,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Graphical Validation

    Test your `compute` function with

    - `(x_0, dx_0, y_0, dy_0, theta_0, dtheta_0, z_0, dz_0) = (5.0, 0.0, 20.0, -1.0, -np.pi/8, 0.0, -M*g, 0.0`),
    - `(x_tf, dx_tf, y_tf, dy_tf, theta_tf, dtheta_tf, z_tf, dz_tf) = (0.0, 0.0, 2/3*l, 0.0,     0.0, 0.0, -M*g, 0.0`),
    - `tf = 10.0`.

    Make the graph of the relevant variables as a function of time, then make an animation out of the same result. Comment and iterate if necessary!
    """)
    return


@app.cell
def _(M, compute, g, l, mo, np, plt):
    def exact_linearization_validation():
        tf = 10.0

        fun = compute(
            5.0, 0.0, 20.0, -1.0, -np.pi / 8, 0.0, -M * g, 0.0,
            0.0, 0.0, 2 / 3 * l, 0.0, 0.0, 0.0, -M * g, 0.0,
            tf,
        )

        t = np.linspace(0.0, tf, 1000)
        values = np.array([fun(ti) for ti in t])

        x, dx, y, dy = values[:, 0], values[:, 1], values[:, 2], values[:, 3]
        theta, dtheta = values[:, 4], values[:, 5]
        z, dz = values[:, 6], values[:, 7]
        f, phi = values[:, 8], values[:, 9]

        print("État initial calculé :")
        print(values[0])

        print("\nÉtat final calculé :")
        print(values[-1])

        print("\nVérifications :")
        print(f"min(z) = {np.min(z):.6f}")
        print(f"max(z) = {np.max(z):.6f}")
        print(f"min(f) = {np.min(f):.6f}")
        print(f"max(f) = {np.max(f):.6f}")
        print(f"max |theta| = {np.max(np.abs(theta)):.6f} rad")
        print(f"max |phi| = {np.max(np.abs(phi)):.6f} rad")

        target_initial = np.array([5.0, 0.0, 20.0, -1.0, -np.pi / 8, 0.0, -M * g, 0.0])
        target_final = np.array([0.0, 0.0, 2 / 3 * l, 0.0, 0.0, 0.0, -M * g, 0.0])
    
        print("Erreur initiale :", np.linalg.norm(values[0, :8] - target_initial))
        print("Erreur finale :", np.linalg.norm(values[-1, :8] - target_final))
        print("min z(t) :", np.min(z))
        print("max |phi(t)| :", np.max(np.abs(phi)))
        fig, axes = plt.subplots(5, 1, sharex=True, figsize=(12, 12))

        axes[0].plot(t, x, label=r"$x(t)$")
        axes[0].plot(t, y, label=r"$y(t)$")
        axes[0].grid(True)
        axes[0].legend()

        axes[1].plot(t, dx, label=r"$\dot{x}(t)$")
        axes[1].plot(t, dy, label=r"$\dot{y}(t)$")
        axes[1].grid(True)
        axes[1].legend()

        axes[2].plot(t, theta, label=r"$\theta(t)$")
        axes[2].plot(t, dtheta, label=r"$\dot{\theta}(t)$")
        axes[2].grid(True)
        axes[2].legend()

        axes[3].plot(t, z, label=r"$z(t)$")
        axes[3].plot(t, dz, label=r"$\dot z(t)$")
        axes[3].axhline(0.0, linestyle="--", label=r"$z=0$")
        axes[3].grid(True)
        axes[3].legend()

        axes[4].plot(t, f, label=r"$f(t)$")
        axes[4].plot(t, phi, label=r"$\phi(t)$")
        axes[4].set_xlabel("time $t$")
        axes[4].grid(True)
        axes[4].legend()

        return mo.center(fig)

    exact_linearization_validation()
    return


@app.cell
def _():
    return


@app.cell
def _(M, booster_anim, compute, g, l, mo, np, world):
    def exact_linearization_animation():
        tf = 10.0

        fun = compute(
            5.0, 0.0, 20.0, -1.0, -np.pi / 8, 0.0, -M * g, 0.0,
            0.0, 0.0, 2 / 3 * l, 0.0, 0.0, 0.0, -M * g, 0.0,
            tf,
        )

        def x_fun(t):
            return fun(t)[0]

        def y_fun(t):
            return fun(t)[2]

        def theta_fun(t):
            return fun(t)[4]

        def f_fun(t):
            return fun(t)[8]

        def phi_fun(t):
            return fun(t)[9]

        return mo.Html(
            world(
                [-2, 7, -2, 22],
                booster_anim(x_fun, y_fun, theta_fun, f_fun, phi_fun, T=tf),
            )
        ).center()

    exact_linearization_animation()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Commentaire sur la validation numérique

    Les valeurs calculées au temps initial et au temps final correspondent bien aux contraintes imposées. Les petites différences visibles, par exemple les valeurs de l’ordre de \(10^{-14}\), sont des erreurs numériques dues à la résolution du système linéaire définissant les polynômes et aux calculs en virgule flottante.

    Les erreurs globales sont :
    \[
    \|s(0)-s_0\| \approx 5.0\times 10^{-15},
    \qquad
    \|s(t_f)-s_f\| \approx 1.8\times 10^{-13}.
    \]
    Ces valeurs sont négligeables à l’échelle du problème, donc les conditions de bord sont bien respectées.

    On vérifie aussi que
    \[
    z(t)<0
    \]
    sur toute la trajectoire, puisque
    \[
    \min z(t)\approx -2.183,
    \qquad
    \max z(t)\approx -0.395.
    \]
    L’hypothèse utilisée dans l’inversion \(T^{-1}\), à savoir \(z<0\), reste donc valide pendant tout le mouvement.

    Les commandes reconstruites restent également raisonnables :
    \[
    0.663 \leq f(t) \leq 2.184,
    \]
    donc la poussée reste positive. De plus,
    \[
    \max |\phi(t)|\approx 0.769\text{ rad}<\frac{\pi}{2},
    \]
    ce qui signifie que l’orientation de la poussée reste dans un domaine acceptable.

    Enfin,
    \[
    \max |\theta(t)|\approx 1.348\text{ rad}<\frac{\pi}{2}.
    \]
    Le booster reste donc dans une plage angulaire cohérente avec les hypothèses géométriques du modèle.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Conclusion

    La trajectoire construite par linéarisation exacte est admissible. Les conditions initiales et finales sont satisfaites avec des erreurs numériques négligeables, de l’ordre de \(10^{-13}\) au maximum.

    La contrainte essentielle \(z(t)<0\) est vérifiée sur tout l’intervalle de temps, ce qui garantit que la transformation inverse utilisée pour reconstruire l’état du booster reste bien définie.

    Les commandes obtenues sont cohérentes : la poussée \(f(t)\) reste positive et l’angle de poussée \(\phi(t)\) reste strictement inférieur à \(\pi/2\) en valeur absolue. L’angle du booster \(\theta(t)\) reste aussi inférieur à \(\pi/2\), ce qui confirme que la trajectoire reste dans le domaine de validité attendu.
    """)
    return


if __name__ == "__main__":
    app.run()
