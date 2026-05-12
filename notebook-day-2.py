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

    return la, np, plt, scipy


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


@app.cell(hide_code=True)
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


@app.cell(hide_code=True)
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
    mo.md(r"""
    Pour que le système soit à l'équilibre, toutes les accélérations doivent être nulles :
    $$\ddot{x} = 0, \quad \ddot{y} = 0, \quad \ddot{\theta} = 0$$

    À partir de l'équation de rotation :
    $$-\frac{lf}{2J} \sin(\phi) = 0$$

    Étant donné que $f > 0$ et que les constantes physiques $l$ et $J$ sont positives, nous devons avoir :
    $$\sin(\phi) = 0$$
    Sous la contrainte $|\phi| < \pi/2$, la seule solution est :
    **$\phi = 0$**

    En injectant $\phi = 0$ dans les deux premières équations :


    $$-\frac{f}{M} \sin(\theta + 0) = 0 \implies \sin(\theta) = 0$$
    Et puisque $|\theta| < \pi/2$, on obtient :
    **$\theta = 0$**


    $$\frac{f}{M} \cos(0 + 0) - g = 0 \implies \frac{f}{M} = g$$
    D'où la valeur de la force :
    **$f = Mg$**

    *Conclusion :* L'ensemble des équilibres est :
    $$
    s^* = (x^*,\;0,\;y^*,\;0,\;0,\;0),\quad f^* = Mg,\quad \phi^* = 0,
    $$
    où $(x^*, y^*) \in \mathbb{R}^2$ est arbitraire : le booster tient verticalement à n'importe quelle position, tuyère droite, poussée égale au poids.
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
    mo.md(r"""
    ### Définition des variables d'erreur
    On définit les écarts par rapport à la configuration d'équilibre générique :
    * $\Delta x = x - x_e$
    * $\Delta y = y - y_e$
    * $\Delta \theta = \theta - 0 = \theta$
    * $\Delta f = f - Mg$
    * $\Delta \phi = \phi - 0 = \phi$

    ---

    Pour obtenir les équations linéaires, on utilise les approximations au premier ordre pour les petits angles ($\sin \alpha \approx \alpha$, $\cos \alpha \approx 1$) et on néglige les produits d'erreurs ($\Delta f \cdot \Delta \theta \approx 0$).

    #### Équation horizontale ($\Delta \ddot{x}$)
    $$\Delta \ddot{x} = -\frac{(Mg + \Delta f)}{M} \sin(\Delta \theta + \Delta \phi)$$
    $$\Delta \ddot{x} \approx -\frac{Mg + \Delta f}{M} (\Delta \theta + \Delta \phi) \approx -g(\Delta \theta + \Delta \phi)$$

    #### Équation verticale ($\Delta \ddot{y}$)
    $$\Delta \ddot{y} = \frac{(Mg + \Delta f)}{M} \cos(\Delta \theta + \Delta \phi) - g$$
    $$\Delta \ddot{y} \approx \frac{Mg + \Delta f}{M}(1) - g = g + \frac{\Delta f}{M} - g = \frac{\Delta f}{M}$$

    #### Équation de rotation ($\Delta \ddot{\theta}$)
    $$\Delta \ddot{\theta} = -\frac{l(Mg + \Delta f)}{2J} \sin(\Delta \phi)$$
    $$\Delta \ddot{\theta} \approx -\frac{l(Mg + \Delta f)}{2J} \Delta \phi \approx -\frac{lMg}{2J} \Delta \phi$$

    ---

    ### Système d'équations linéaires final
    Les équations différentielles ordinaires qui gouvernent approximativement le système au voisinage de l'équilibre sont :

    $$
    \begin{cases}
    \Delta \ddot{x} = -g \Delta \theta - g \Delta \phi \\
    \Delta \ddot{y} = \frac{1}{M} \Delta f \\
    \Delta \ddot{\theta} = -\frac{lMg}{2J} \Delta \phi
    \end{cases}
    $$
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
    Le système est représenté sous la forme :
    $$\mathbf{\dot{s}} = A\mathbf{s} + B\mathbf{u}$$

    ### 1. Définition du vecteur d'état et des matrices

    On définit le vecteur d'état $\mathbf{s}$ et le vecteur d'entrée $\mathbf{u}$ :
    $$\mathbf{s} = \begin{bmatrix} \Delta x \\ \Delta \dot{x} \\ \Delta y \\ \Delta \dot{y} \\ \Delta \theta \\ \Delta \dot{\theta} \end{bmatrix}, \quad \mathbf{u} = \begin{bmatrix} \Delta f \\ \Delta \phi \end{bmatrix}$$

    #### Matrice $A$ ($6 \times 6$)
    $$A = \begin{bmatrix}
    0 & 1 & 0 & 0 & 0 & 0 \\
    0 & 0 & 0 & 0 & -g & 0 \\
    0 & 0 & 0 & 1 & 0 & 0 \\
    0 & 0 & 0 & 0 & 0 & 0 \\
    0 & 0 & 0 & 0 & 0 & 1 \\
    0 & 0 & 0 & 0 & 0 & 0
    \end{bmatrix}$$

    #### Matrice $B$ ($6 \times 2$)
    $$B = \begin{bmatrix}
    0 & 0 \\
    0 & -g \\
    0 & 0 \\
    \frac{1}{M} & 0 \\
    0 & 0 \\
    0 & -\frac{lMg}{2J}
    \end{bmatrix}$$

    ---
    """)
    return


@app.cell
def _(J, M, g, l, np):
    A = np.array([
        [0, 1, 0, 0,  0, 0],  
        [0, 0, 0, 0, -g, 0],  
        [0, 0, 0, 1,  0, 0],  
        [0, 0, 0, 0,  0, 0],  
        [0, 0, 0, 0,  0, 1],  
        [0, 0, 0, 0,  0, 0]   
    ])

    B = np.array([
        [0, 0],             
        [0, -g],              
        [0, 0],              
        [1/M, 0],             
        [0, 0],               
        [0, -(l*M*g)/(2*J)]   
    ])

    print("Matrice A :")
    print(A)
    print("\nMatrice B :")
    print(B)
    return A, B


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
    Pour qu'un équilibre soit **asymptotiquement stable**, toutes les valeurs propres ($\lambda$) de la matrice $A$ doivent avoir une partie réelle strictement négative ($\text{Re}(\lambda) < 0$).

    ### 1. Analyse des valeurs propres
    En utilisant la matrice $A$ définie pour le vecteur $s = [\Delta x, \Delta \dot{x}, \Delta y, \Delta \dot{y}, \Delta \theta, \Delta \dot{\theta}]^T$ :

    $$A = \begin{bmatrix}
    0 & 1 & 0 & 0 & 0 & 0 \\
    0 & 0 & 0 & 0 & -g & 0 \\
    0 & 0 & 0 & 1 & 0 & 0 \\
    0 & 0 & 0 & 0 & 0 & 0 \\
    0 & 0 & 0 & 0 & 0 & 1 \\
    0 & 0 & 0 & 0 & 0 & 0
    \end{bmatrix}$$

    $A$ est une matrice triangulaire dont les éléments diagonaux sont tous nuls.
    Donc Le système possède six valeurs propres toutes égales à zéro ($\lambda_{1..6} = 0$).

    ### 2. Conclusion
    L'équilibre générique n'est **pas asymptotiquement stable** car les valeurs propres n'ont pas de partie réelle strictement négative.

    **Interprétation :**
    * Le booster est naturellement instable.
    * Sans l'ajout d'une loi de commande (feedback), toute perturbation sur l'angle ou la vitesse entraînera une dérive ou une chute du système.
    """)
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
    ### 1. Condition de commandabilité
    Un système linéaire invariant dans le temps, défini par l'équation d'état $\dot{s} = As + Bu$, est dit **entièrement commandable** si et seulement si la matrice de commandabilité $\mathcal{C}$ est de **rang plein**. Pour notre système de dimension $n=6$, la matrice $\mathcal{C}$ est définie par :
    $$\mathcal{C} = [B \quad AB \quad A^2B \quad A^3B \quad A^4B \quad A^5B]$$
    Si $\text{rang}(\mathcal{C}) = 6$, il est possible de transférer le système de n'importe quel état initial vers n'importe quel état final (comme l'équilibre de l'atterrissage) en un temps fini.

    ### 2. Vérification du rang de $\mathcal{C}$
    Le code suivant permet de calculer la matrice de commandabilité et d'en vérifier le rang mathématiquement :
    """)
    return


@app.cell
def _(A, B, la, np):
    # Calcul de la matrice de commandabilité C
    n = A.shape[0]
    C = B
    for i in range(1, n):
        C = np.hstack((C, np.linalg.matrix_power(A, i) @ B))

    # Vérification du rang
    rang_C = la.matrix_rank(C)
    print(f"Rang de la matrice C : {rang_C}")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 3. Analyse du système

    Le modèle linéarisé est entièrement commandable car le rang de la matrice $\mathcal{C}$ est égal à 6. Cette analyse permet de tirer les conclusions suivantes :

    * **Découplage de la poussée** : L'entrée $\Delta f$ commande directement l'altitude $\Delta y$ (translation verticale), permettant de gérer la descente indépendamment des mouvements latéraux.
    * **Couplage dynamique** : L'entrée $\Delta \phi$ ne commande pas uniquement l'angle $\theta$ ; grâce au couplage présent dans la matrice $A$, elle permet également de contrôler la position latérale $x$.
    * **Faisabilité du contrôle** : La commandabilité totale garantit qu'il est mathématiquement possible de concevoir une loi de commande capable de stabiliser le booster pour un atterrissage vertical réussi.
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
    # Système de dynamique latérale réduit

    En limitant l'étude à la position latérale $x$ et à l'inclinaison $\theta$, nous simplifions le système pour nous concentrer sur le contrôle de la trajectoire horizontale. Le vecteur d'état réduit est $s_{red} = [\Delta x, \Delta \dot{x}, \Delta \theta, \Delta \dot{\theta}]^T$ et l'unique entrée de commande est $u = [\Delta \phi]$ (en fixant $f = Mg$).

    ### Définition des équations et des matrices réduites $A_{red}$ et $B_{red}$

    Les équations différentielles ordinaires qui gouvernent ce système réduit sont :

    $$\Delta \dot{x} = \Delta \dot{x}$$
    $$\Delta \ddot{x} = -g \Delta \theta - g \Delta \phi$$
    $$\Delta \dot{\theta} = \Delta \dot{\theta}$$
    $$\Delta \ddot{\theta} = -\frac{lMg}{2J} \Delta \phi$$

    Sous forme d'état standard $\dot{s}_{red} = A_{red}s_{red} + B_{red}u$, les matrices sont définies comme suit :

    #### Matrice d'état réduite $A_{red}$ ($4 \times 4$)
    $$A_{red} = \begin{bmatrix}
    0 & 1 & 0 & 0 \\
    0 & 0 & -g & 0 \\
    0 & 0 & 0 & 1 \\
    0 & 0 & 0 & 0
    \end{bmatrix}$$

    #### Matrice de commande réduite $B_{red}$ ($4 \times 1$)
    $$B_{red} = \begin{bmatrix}
    0 \\
    -g \\
    0 \\
    -\frac{lMg}{2J}
    \end{bmatrix}$$
    """)
    return


@app.cell
def _(J, M, g, l, la, np):
    # Définition des matrices avec la nouvelle notation 'red'
    A_red = np.array([
        [0, 1,  0, 0],
        [0, 0, -g, 0],
        [0, 0,  0, 1],
        [0, 0,  0, 0]
    ])

    B_red = np.array([
        [0],
        [-g],
        [0],
        [-(l * M * g) / (2 * J)]
    ])

    # Calcul de la matrice de commandabilité C = [B_red, A_red*B_red, ...]
    N = A_red.shape[0]
    C_red = B_red
    for j in range(1, N):
        term = np.linalg.matrix_power(A_red, j) @ B_red
        C_red = np.hstack((C_red, term))

    # Vérification du rang de la matrice de commandabilité
    rang_C_red = la.matrix_rank(C_red)

    print("Matrice A_red :\n", A_red)
    print("\nMatrice B_red :\n", B_red)
    print(f"\nRang de la matrice de commandabilité : {rang_C_red}")
    print(f"Le système réduit est-il commandable ? {rang_C_red == N}")
    return A_red, B_red


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ###  Analyse du système

    Le modèle linéarisé réduit est **entièrement commandable** car le rang de la matrice de commandabilité est égal à 4. Cette analyse permet de tirer les conclusions suivantes :

    * **Accessibilité des états** : Bien que le système ne dispose plus que d'une seule entrée ($\Delta \phi$), celle-ci est suffisante pour piloter l'ensemble des quatre variables d'état latérales du booster.
    * **Couplage dynamique** : L'entrée $\Delta \phi$ commande directement l'accélération angulaire $\Delta \ddot{\theta}$, mais elle agit aussi sur la position latérale $x$ via l'angle $\theta$ et le terme de couplage $-g$ dans la matrice $A_{red}$.
    * **Faisabilité du contrôle** : La commandabilité totale confirme qu'il est mathématiquement possible de concevoir une loi de commande pour stabiliser le booster horizontalement en utilisant uniquement l'orientation du moteur.
    """)
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


@app.cell
def _(A_red, np, plt):

    from scipy.integrate import odeint


    s0 = [0.0, 0.0, np.pi/4, 0.0] 
    t = np.linspace(0, 5, 5000)

    # 2. Fonction de dynamique (utilise A_red déjà définie)
    def system_dynamics_simple(s, t_vector):
        return A_red @ s

    # 3. Simulation
    sol = odeint(system_dynamics_simple, s0, t)
    x_t = sol[:, 0]
    theta_t = sol[:, 2]*180*(1/np.pi)

    # 4. Tracé des graphiques
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

    # Graphique x(t)
    ax1.plot(t, x_t, color='blue', lw=2, label='$x(t)$')
    ax1.set_title('Position latérale $x(t)$')
    ax1.set_xlabel('Temps (s)')
    ax1.set_ylabel('Distance (m)')
    ax1.grid(True, linestyle='--')
    ax1.legend()

    # Graphique theta(t)
    ax2.plot(t, theta_t, color='red', lw=2, label='$\\theta(t)$')
    ax2.axhline(y=s0[2], color='black', linestyle=':', label='Initial $\\theta_0$')
    ax2.set_title('Inclinaison $\\theta(t)$')
    ax2.set_xlabel('Temps (s)')
    ax2.set_ylabel('Angle (rad)')
    ax2.grid(True, linestyle='--')
    ax2.legend()

    plt.tight_layout()
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 2. Observation et explication

    **Ce que l'on observe :**
    * **L'angle $\theta(t)$ reste constant** : La ligne rouge est parfaitement horizontale à $\pi/4$. Comme l'entrée de contrôle $\phi$ est nulle, rien ne modifie la rotation.
    * **La position $x(t)$ diverge** : On observe une courbe parabolique qui descend vers les valeurs négatives. Le booster dérive de plus en plus vite.

    **Explication théorique :**
    1.  **Équilibre instable** : Sans contrôle ($\phi = 0$), l'accélération angulaire est nulle. Le booster conserve son inclinaison initiale.
    2.  **Force latérale constante** : Comme le booster est penché ($\theta = \pi/4$), la poussée du moteur n'est plus purement verticale. Elle génère une accélération latérale constante $\Delta \ddot{x} = -g \Delta \theta$.
    3.  **Mouvement uniformément accéléré** : Une accélération constante crée une trajectoire parabolique pour la position $x(t)$, ce qui explique pourquoi le booster s'éloigne indéfiniment de sa cible.

    **Conclusion :** Le système est **instable**. Sans une correction active via $\phi$, une simple erreur d'inclinaison initiale détruit la précision de l'atterrissage.
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
    mo.md(r"""
    On cherche d’abord une commande simple qui stabilise seulement l’angle :

    $$
    K =
    \begin{bmatrix}
    0 & 0 & k_\theta & k_\omega
    \end{bmatrix}
    $$

    avec :

    $$
    \Delta \phi = -K s_{red}.
    $$

    Ici, on ne contrôle pas directement $x$ ni $\dot{x}$

    La dynamique angulaire linéarisée est :

    $$
    \Delta \ddot{\theta}
    =
    -\frac{\ell Mg}{2J}\Delta \phi.
    $$

    Comme :

    $$
    \Delta \phi =
    -k_\theta \Delta \theta
    -k_\omega \Delta \dot{\theta},
    $$

    on obtient :

    $$
    \Delta \ddot{\theta}
    =
    \frac{\ell Mg}{2J}
    \left(
    k_\theta \Delta \theta
    +
    k_\omega \Delta \dot{\theta}
    \right).
    $$

    On veut une dynamique stable du second ordre :

    $$
    \Delta \ddot{\theta}
    +
    2\zeta\omega_n \Delta \dot{\theta}
    +
    \omega_n^2 \Delta \theta
    =0.
    $$

    Donc on choisit :

    $$
    k_\theta =
    -\frac{\omega_n^2}{\ell Mg/(2J)},
    \qquad
    k_\omega =
    -\frac{2\zeta\omega_n}{\ell Mg/(2J)}.
    $$


    Ici, $\omega_n$ règle la vitesse de convergence et $\zeta$ règle l’amortissement.

    On choisit un amortissement élevé :

    $$
    \zeta = 0.9
    $$

    afin d’éviter les oscillations et de garder $|\Delta \theta| < \pi/2$.

    On veut que l’angle converge en moins de 20 secondes. Pour un système du second ordre, le temps de stabilisation est approximativement :

    $$
    T_s \approx \frac{4}{\zeta\omega_n}.
    $$

    Ensuite, on choisit $\omega_n$ pour avoir un temps de stabilisation inférieur à 20 secondes. Avec :

    $$
    \omega_n = 0.35,
    $$

    on obtient :

    $$
    T_s \approx \frac{4}{0.9 \times 0.35}
    \approx 12.7 \text{ s}.
    $$


    Donc : $\zeta$ = 0.9 et $\omega_n$ = 0.35

    Avec :

    $$
    \frac{\ell Mg}{2J}=3,
    $$

    les gains sont :

    $$
    k_\theta =
    -\frac{\omega_n^2}{3},
    \qquad
    k_\omega =
    -\frac{2\zeta\omega_n}{3}.
    $$

    Donc :

    $$
    k_\theta \approx -0.0408,
    \qquad
    k_\omega \approx -0.21.
    $$

    A.N :

    $$
    \frac{\ell Mg}{2J}=3.
    $$

    Donc :

    $$
    K =
    \begin{bmatrix}
    0 & 0 & -0.0408 & -0.21
    \end{bmatrix}.
    $$
    """)
    return


@app.cell
def _(J, M, g, l, np):
    omega_n = 0.35
    zeta = 0.9

    alpha = (l * M * g) / (2 * J)

    k_theta = -(omega_n ** 2) / alpha
    k_omega = -(2 * zeta * omega_n) / alpha

    K_manual = np.array([[0.0, 0.0, k_theta, k_omega]])

    print("alpha =", alpha)
    print("K_manual =", K_manual)
    return (K_manual,)


@app.cell
def _(A_red, B_red, np, scipy):
    def simulate_linear_controller(K, T=20.0):
        t_span = [0.0, T]
        s0 = np.array([0.0, 0.0, np.pi / 4, 0.0])

        A_cl = A_red - B_red @ K

        def dyn(t, s):
            return A_cl @ s

        sol = scipy.integrate.solve_ivp(
            dyn,
            t_span,
            s0,
            dense_output=True,
            max_step=0.01,
        )

        t = np.linspace(0.0, T, 2000)
        s = sol.sol(t)
        phi = -(K @ s).flatten()

        return t, s, phi, A_cl

    return (simulate_linear_controller,)


@app.cell
def _(K_manual, la, np, plt, simulate_linear_controller):
    t_manual, s_manual, phi_manual, Acl_manual = simulate_linear_controller(K_manual)

    plt.figure(figsize=(12, 4))

    plt.subplot(1, 3, 1)
    plt.plot(t_manual, s_manual[0])
    plt.title(r"$\Delta x(t)$")
    plt.grid(True)

    plt.subplot(1, 3, 2)
    plt.plot(t_manual, s_manual[2])
    plt.axhline(np.pi / 2, ls="--")
    plt.axhline(-np.pi / 2, ls="--")
    plt.title(r"$\Delta \theta(t)$")
    plt.grid(True)

    plt.subplot(1, 3, 3)
    plt.plot(t_manual, phi_manual)
    plt.axhline(np.pi / 2, ls="--")
    plt.axhline(-np.pi / 2, ls="--")
    plt.title(r"$\Delta \phi(t)$")
    plt.grid(True)

    plt.tight_layout()
    plt.show()

    eig_manual = la.eigvals(Acl_manual)

    print("Valeurs propres :")
    print(eig_manual)

    print("Stable asymptotiquement ?")
    print(np.all(np.real(eig_manual) < 0))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Les simulations permettent de vérifier que :

    - $\Delta \theta(t) \to 0$ en environ 20 secondes,
    - $|\Delta \theta(t)| < \pi/2$,
    - $|\Delta \phi(t)| < \pi/2$.

    Cependant, le modèle fermé final n’est pas asymptotiquement stable pour tout l’état réduit, car $x$ et $\dot{x}$ ne sont pas stabilisés.
    """)
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
    mo.md(r"""
    ### On cherche maintenant une commande complète :

    $$
    K_{pp}
    =
    \begin{bmatrix}
    k_x & k_v & k_\theta & k_\omega
    \end{bmatrix}
    $$

    avec :

    $$
    \Delta \phi = -K_{pp}s_{red}.
    $$

    Le système fermé est :

    $$
    \dot{s}_{red}
    =
    (A_{red} - B_{red}K_{pp})s_{red}.
    $$

    Cette fois, on veut stabiliser tout l’état :

    $$
    \Delta x \to 0,
    \qquad
    \Delta \theta \to 0.
    $$

    Pour cela, on choisit directement les pôles du système fermé.

    Les pôles doivent avoir des parties réelles négatives pour garantir la stabilité asymptotique.

    Il faut faire un choix de poles qui donne une dynamique assez rapide pour converger en moins de 20 secondes, mais pas trop agressive afin de garder :

    $$
    |\Delta \phi| < \frac{\pi}{2}.
    $$

    (Voir code tests poles au dessous)

    Ensuite, on utilise le placement de pôles pour calculer automatiquement $K_{pp}$ tel que les valeurs propres de :

    $$
    A_{red} - B_{red}K_{pp}
    $$

    soient les pôles choisis.
    """)
    return


@app.cell
def _(A_red, B_red, la, np, plt, scipy):
    from scipy.signal import place_poles

    def pole_placement(A_red, B_red):
        # ------------------------------------------------------------
        # Objectif :
        # Trouver automatiquement des pôles qui stabilisent le système
        # tout en respectant les contraintes :
        #   - theta(t) -> 0
        #   - x(t) -> 0
        #   - |theta(t)| < pi/2
        #   - |phi(t)| < pi/2
        # ------------------------------------------------------------

        # État initial :
        # [Delta x, Delta vx, Delta theta, Delta omega]
        s0 = np.array([0.0, 0.0, np.pi / 4, 0.0])

        # Temps de simulation
        T = 20.0
        t_span = [0.0, T]
        t = np.linspace(0.0, T, 2000)

        # ------------------------------------------------------------
        # Famille de pôles testés :
        # lambda_i = -p * alpha_i
        #
        # p règle la vitesse globale.
        # alpha rend les pôles distincts.

        # ------------------------------------------------------------
        alpha = np.array([1.0, 1.2, 1.4, 1.6])

        # Pour converger en moins de 20 secondes :
        # Ts ≈ 4 / p < 20  =>  p > 0.2
        # On teste donc plusieurs valeurs de p au-dessus de 0.2
        p_values = np.linspace(0.25, 1.2, 30)

        best_result = None

        # ------------------------------------------------------------
        # Recherche automatique du meilleur p
        # ------------------------------------------------------------
        for p in p_values:
            desired_poles = -p * alpha

            try:
                # Calcul du gain K par placement de pôles
                placed = place_poles(A_red, B_red, desired_poles)
                K = placed.gain_matrix

                # Matrice du système fermé
                A_cl = A_red - B_red @ K

                # Dynamique fermée
                def dyn(t_local, s):
                    return A_cl @ s

                # Simulation du modèle linéaire
                sol = scipy.integrate.solve_ivp(
                    dyn,
                    t_span,
                    s0,
                    dense_output=True,
                    max_step=0.01,
                )

                s = sol.sol(t)

                # Commande :
                # Delta phi = -K s
                phi = -(K @ s).flatten()

                # Mesures utilisées pour vérifier les contraintes
                max_phi = np.max(np.abs(phi))
                max_theta = np.max(np.abs(s[2]))

                final_x = abs(s[0, -1])
                final_theta = abs(s[2, -1])

                eigvals = la.eigvals(A_cl)
                stable = np.all(np.real(eigvals) < 0)

                # Contraintes du problème
                constraints_ok = (
                    stable
                    and max_phi < np.pi / 2
                    and max_theta < np.pi / 2
                    and final_x < 1e-2
                    and final_theta < 1e-2
                )

                # Si les contraintes sont respectées, on garde le meilleur
                # Ici, on minimise surtout l'amplitude de la commande phi
                if constraints_ok:
                    score = max_phi + final_x + final_theta

                    if best_result is None or score < best_result["score"]:
                        best_result = {
                            "p": p,
                            "poles": desired_poles,
                            "K": K,
                            "A_cl": A_cl,
                            "t": t,
                            "s": s,
                            "phi": phi,
                            "eigvals": eigvals,
                            "max_phi": max_phi,
                            "max_theta": max_theta,
                            "final_x": final_x,
                            "final_theta": final_theta,
                            "score": score,
                        }

            except Exception:
                # Si un choix de pôles échoue numériquement,
                # on passe simplement au suivant.
                pass


        # ------------------------------------------------------------
        # Résultat final
        # ------------------------------------------------------------
        K_pp = best_result["K"]
        t = best_result["t"]
        s = best_result["s"]
        phi = best_result["phi"]

        print("Meilleur choix trouvé :")
        print("p =", best_result["p"])
        print("pôles =", best_result["poles"])

        print("\nK_pp =")
        print(K_pp)

        print("\nValeurs propres du système fermé :")
        print(best_result["eigvals"])

        print("\nMax |theta| =", best_result["max_theta"])
        print("Max |phi| =", best_result["max_phi"])

        print("\nFinal |x| =", best_result["final_x"])
        print("Final |theta| =", best_result["final_theta"])

        print("\nStable asymptotiquement ?")
        print(np.all(np.real(best_result["eigvals"]) < 0))


    
        plt.figure(figsize=(12, 4))

        plt.subplot(1, 3, 1)
        plt.plot(t, s[0])
        plt.title(r"$\Delta x(t)$")
        plt.xlabel("temps")
        plt.grid(True)

        plt.subplot(1, 3, 2)
        plt.plot(t, s[2])
        plt.axhline(np.pi / 2, ls="--")
        plt.axhline(-np.pi / 2, ls="--")
        plt.title(r"$\Delta \theta(t)$")
        plt.xlabel("temps")
        plt.grid(True)

        plt.subplot(1, 3, 3)
        plt.plot(t, phi)
        plt.axhline(np.pi / 2, ls="--")
        plt.axhline(-np.pi / 2, ls="--")
        plt.title(r"$\Delta \phi(t)$")
        plt.xlabel("temps")
        plt.grid(True)

        plt.tight_layout()
        plt.show()

        return K_pp


    K_pp = pole_placement(A_red, B_red)
    return (K_pp,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Après simulation, on vérifie que :

    - $\Delta x(t) \to 0$ en moins de 20 secondes,
    - $\Delta \theta(t) \to 0$ en moins de 20 secondes,
    - $|\Delta \theta(t)| < \pi/2$,
    - $|\Delta \phi(t)| < \pi/2$,
    - toutes les valeurs propres ont une partie réelle négative.

    Donc le contrôleur par placement de pôles satisfait les conditions demandées et le modèle fermé est asymptotiquement stable.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Controller Tuned with Optimal Control

    Using optimal control, find a gain matrix $K_{oc}$ that satisfies the same set of requirements that the one defined using pole placement.

    Explain how you find the proper design parameters!
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ###On utilise une commande optimale LQR :

    $$
    \Delta \phi = -K_{oc}s_{red}.
    $$

    Le gain $K_{oc}$ est obtenu en minimisant :

    $$
    J =
    \int_0^\infty
    \left(
    s_{red}^TQs_{red}
    +
    \Delta \phi^TR\Delta \phi
    \right)dt.
    $$

    La matrice $Q$ pénalise les erreurs d’état, tandis que $R$ pénalise l’effort de commande.

    Pour éviter un choix arbitraire de $Q$ et $R$, on teste automatiquement plusieurs valeurs.

    On utilise l’hypothèse qualitative suivante :

    - $x$ et $\theta$ doivent être fortement pénalisés, car on veut les ramener à zéro ;
    - $\dot{x}$ et $\dot{\theta}$ sont aussi pénalisés, mais plus faiblement ;
    - $R$ est testé sur plusieurs valeurs, car un grand $R$ donne une commande plus douce.

    Pour chaque choix de $Q$ et $R$, on calcule $K_{oc}$ avec l’équation de Riccati :

    $$
    A_{red}^TP + PA_{red}
    -
    PB_{red}R^{-1}B_{red}^TP
    +
    Q = 0.
    $$

    Puis :

    $$
    K_{oc} = R^{-1}B_{red}^TP.
    $$

    Ensuite, on simule le système fermé et on garde seulement les choix qui vérifient :

    $$
    |\Delta \theta(t)| < \frac{\pi}{2},
    \qquad
    |\Delta \phi(t)| < \frac{\pi}{2},
    $$

    ainsi que :

    $$
    \Delta x(20) \approx 0,
    \qquad
    \Delta \theta(20) \approx 0.
    $$
    """)
    return


@app.cell
def _(A_red, B_red, la, np, plt, scipy):
    from scipy.linalg import solve_continuous_are

    def optimal_control(A_red, B_red):
        # ------------------------------------------------------------
        # Objectif : Trouver automatiquement un contrôleur LQR qui stabilise
        #   - Delta x -> 0
        #   - Delta theta -> 0
        # tout en gardant :
        #   - |theta| < pi/2
        #   - |phi| < pi/2
        # ------------------------------------------------------------

        # État initial demandé :
        # [Delta x, Delta vx, Delta theta, Delta omega]
        s0 = np.array([0.0, 0.0, np.pi / 4, 0.0])

        # Temps de simulation
        T = 20.0
        t_span = [0.0, T]
        t = np.linspace(0.0, T, 2000)

        # ------------------------------------------------------------
        # Familles de matrices Q et R testées
        #
        # Q pénalise les erreurs d'état.
        # R pénalise l'effort de commande phi.
        #
        # On teste plusieurs poids pour :
        #   - x
        #   - theta
        #   - R
        #
        # Les vitesses ont des poids plus faibles.
        # ------------------------------------------------------------

        qx_values = [0.5, 1.0, 2.0, 5.0]
        qtheta_values = [0.5, 1.0, 2.0, 5.0]
        R_values = [5.0, 10.0, 20.0, 40.0, 80.0]

        best_result = None

        # ------------------------------------------------------------
        # Recherche des bons paramètres Q et R
        # ------------------------------------------------------------
        for qx in qx_values:
            for qtheta in qtheta_values:
                for r in R_values:

                    # Matrice Q :
                    # poids fort sur x et theta,
                    # poids plus faible sur les vitesses
                    Q = np.diag([
                        qx,          # poids sur Delta x
                        0.1 * qx,    # poids sur Delta vx
                        qtheta,      # poids sur Delta theta
                        0.1 * qtheta # poids sur Delta omega
                    ])

                    # Matrice R :
                    # plus R est grand, plus la commande phi est pénalisée
                    R = np.array([[r]])

                    try:
                        # Résolution de l'équation de Riccati
                        P = solve_continuous_are(A_red, B_red, Q, R)

                        # Gain LQR
                        K = la.solve(R, B_red.T @ P)

                        # Matrice fermée
                        A_cl = A_red - B_red @ K

                        # Dynamique fermée
                        def dyn(t_local, s):
                            return A_cl @ s

                        # Simulation
                        sol = scipy.integrate.solve_ivp(
                            dyn,
                            t_span,
                            s0,
                            dense_output=True,
                            max_step=0.01,
                        )

                        s = sol.sol(t)

                        # Commande :
                        # Delta phi = -K s
                        phi = -(K @ s).flatten()

                        # Mesures utiles
                        eigvals = la.eigvals(A_cl)
                        stable = np.all(np.real(eigvals) < 0)

                        max_phi = np.max(np.abs(phi))
                        max_theta = np.max(np.abs(s[2]))

                        final_x = abs(s[0, -1])
                        final_theta = abs(s[2, -1])

                        # Contraintes demandées
                        constraints_ok = (
                            stable
                            and max_phi < np.pi / 2
                            and max_theta < np.pi / 2
                            and final_x < 1e-2
                            and final_theta < 1e-2
                        )

                        # Score :
                        # on cherche une commande douce,
                        # mais qui finit proche de l'équilibre
                        if constraints_ok:
                            score = max_phi + final_x + final_theta

                            if best_result is None or score < best_result["score"]:
                                best_result = {
                                    "Q": Q,
                                    "R": R,
                                    "K": K,
                                    "A_cl": A_cl,
                                    "eigvals": eigvals,
                                    "t": t,
                                    "s": s,
                                    "phi": phi,
                                    "max_phi": max_phi,
                                    "max_theta": max_theta,
                                    "final_x": final_x,
                                    "final_theta": final_theta,
                                    "score": score,
                                }

                    except Exception:
  
                        pass


        # ------------------------------------------------------------
        if best_result is None:
            print("Aucun choix de Q et R satisfaisant trouvé.")
            return None

        # ------------------------------------------------------------
        K_oc = best_result["K"]
        t = best_result["t"]
        s = best_result["s"]
        phi = best_result["phi"]

        print("Meilleur choix trouvé :")
        print("\nQ =")
        print(best_result["Q"])

        print("\nR =")
        print(best_result["R"])

        print("\nK_oc =")
        print(K_oc)

        print("\nValeurs propres du système fermé :")
        print(best_result["eigvals"])

        print("\nMax |theta| =", best_result["max_theta"])
        print("Max |phi| =", best_result["max_phi"])

        print("\nFinal |x| =", best_result["final_x"])
        print("Final |theta| =", best_result["final_theta"])

        print("\nStable asymptotiquement ?")
        print(np.all(np.real(best_result["eigvals"]) < 0))

        # ------------------------------------------------------------
        plt.figure(figsize=(12, 4))

        plt.subplot(1, 3, 1)
        plt.plot(t, s[0])
        plt.title(r"$\Delta x(t)$")
        plt.xlabel("temps")
        plt.grid(True)

        plt.subplot(1, 3, 2)
        plt.plot(t, s[2])
        plt.axhline(np.pi / 2, ls="--")
        plt.axhline(-np.pi / 2, ls="--")
        plt.title(r"$\Delta \theta(t)$")
        plt.xlabel("temps")
        plt.grid(True)

        plt.subplot(1, 3, 3)
        plt.plot(t, phi)
        plt.axhline(np.pi / 2, ls="--")
        plt.axhline(-np.pi / 2, ls="--")
        plt.title(r"$\Delta \phi(t)$")
        plt.xlabel("temps")
        plt.grid(True)

        plt.tight_layout()
        plt.show()

        return K_oc


    K_oc = optimal_control(A_red, B_red)
    return (K_oc,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    on a vérifié que :

    - $\Delta x(t) \to 0$ en moins de 20 secondes,
    - $\Delta \theta(t) \to 0$ en moins de 20 secondes,
    - $|\Delta \phi(t)| < \pi/2$,
    - les valeurs propres de $A_{red} - B_{red}K_{oc}$ ont une partie réelle négative.

    Donc le contrôleur optimal obtenu satisfait les conditions demandées.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Validation

    Test the two control strategies (pole placement and optimal control) on the "true" (nonlinear) model with an animation. Check that both controllers achieve their goal; otherwise, go back to the drawing board and tweak the design parameters until they do!
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    On teste maintenant les deux contrôleurs sur le modèle non linéaire.

    Les contrôleurs ont été conçus avec le modèle latéral linéarisé :

    $$
    s_{red} =
    \begin{bmatrix}
    x \\
    \dot{x} \\
    \theta \\
    \dot{\theta}
    \end{bmatrix}.
    $$

    Dans le modèle non linéaire, l’état complet est :

    $$
    s =
    \begin{bmatrix}
    x \\
    \dot{x} \\
    y \\
    \dot{y} \\
    \theta \\
    \dot{\theta}
    \end{bmatrix}.
    $$

    On extrait donc seulement l’état latéral :

    $$
    s_{lat} =
    \begin{bmatrix}
    x \\
    \dot{x} \\
    \theta \\
    \dot{\theta}
    \end{bmatrix}.
    $$

    Puis on applique :

    $$
    \phi = -Ks_{lat}.
    $$

    On garde une poussée constante :

    $$
    f = Mg.
    $$

    On teste successivement :

    - le contrôleur par placement de pôles $K_{pp}$,
    - le contrôleur optimal $K_{oc}$.

    Pour éviter une orientation irréaliste du moteur, on limite la commande :

    $$
    -\frac{\pi}{2} < \phi < \frac{\pi}{2}.
    $$
    """)
    return


@app.cell
def _(M, booster_anim, g, mo, np, plt, redstart_solve, world):
    def validation_nonlinear_controller(K, title):
        T = 20.0
        t_span = [0.0, T]

        # état initial : x, vx, y, vy, theta, omega
        y0 = [0.0, 0.0, 10.0, 0.0, np.pi / 4, 0.0]

        def f_phi(t, state):
            x, vx, y, vy, theta, omega = state

            s_lat = np.array([x, vx, theta, omega])
            phi = float(-(K @ s_lat)[0])

            # On garde phi dans l'intervalle autorisé
            phi = np.clip(phi, -np.pi / 2 + 1e-3, np.pi / 2 - 1e-3)

            f = M * g

            return np.array([f, phi])

        sol = redstart_solve(t_span, y0, f_phi)

        t = np.linspace(0.0, T, 2000)
        states = sol(t)

        phi_values = np.array([
            f_phi(t[i], states[:, i])[1]
            for i in range(len(t))
        ])

        # Graphes
        plt.figure(figsize=(12, 4))

        plt.subplot(1, 3, 1)
        plt.plot(t, states[0])
        plt.title(title + r" : $x(t)$")
        plt.xlabel("temps")
        plt.grid(True)

        plt.subplot(1, 3, 2)
        plt.plot(t, states[4])
        plt.axhline(np.pi / 2, ls="--")
        plt.axhline(-np.pi / 2, ls="--")
        plt.title(title + r" : $\theta(t)$")
        plt.xlabel("temps")
        plt.grid(True)

        plt.subplot(1, 3, 3)
        plt.plot(t, phi_values)
        plt.axhline(np.pi / 2, ls="--")
        plt.axhline(-np.pi / 2, ls="--")
        plt.title(title + r" : $\phi(t)$")
        plt.xlabel("temps")
        plt.grid(True)

        plt.tight_layout()
        plt.show()

        # Animation
        x_fun = lambda tau: sol(tau)[0]
        y_fun = lambda tau: sol(tau)[2]
        theta_fun = lambda tau: sol(tau)[4]
        f_fun = lambda tau: f_phi(tau, sol(tau))[0]
        phi_fun = lambda tau: f_phi(tau, sol(tau))[1]

        anim = mo.Html(
            world(
                [-8, 8, -2, 12],
                booster_anim(x_fun, y_fun, theta_fun, f_fun, phi_fun, T=T),
            )
        ).center()

        print(title)
        print("Max |phi| =", np.max(np.abs(phi_values)))
        print("État final :")
        print(states[:, -1])

        return anim

    return (validation_nonlinear_controller,)


@app.cell
def _(K_pp, validation_nonlinear_controller):
    validation_nonlinear_controller(K_pp, "Placement de pôles")
    return


@app.cell
def _(K_oc, validation_nonlinear_controller):
    validation_nonlinear_controller(K_oc, "Commande optimale LQR")
    return


@app.cell
def _(A_red, B_red, K_oc, K_pp, la, np, scipy):
    def compare_methods(A_red, B_red, K_pp, K_oc):

        methods = {
            "Placement de pôles": K_pp,
            "Commande optimale LQR": K_oc,
        }

        s0 = np.array([0.0, 0.0, np.pi / 4, 0.0])
        T = 20.0
        t_span = [0.0, T]
        t = np.linspace(0.0, T, 2000)

        rows = []

        for name, K in methods.items():
            A_cl = A_red - B_red @ K

            def dyn(t_local, s):
                return A_cl @ s

            sol = scipy.integrate.solve_ivp(
                dyn,
                t_span,
                s0,
                dense_output=True,
                max_step=0.01,
            )

            s = sol.sol(t)
            phi = -(K @ s).flatten()

            eigvals = la.eigvals(A_cl)

            max_theta = np.max(np.abs(s[2]))
            max_phi = np.max(np.abs(phi))

            final_x = abs(s[0, -1])
            final_theta = abs(s[2, -1])

            stable = np.all(np.real(eigvals) < 0)

            rows.append({
                "Méthode": name,
                "Max |theta|": max_theta,
                "Max |phi|": max_phi,
                "|x(20)|": final_x,
                "|theta(20)|": final_theta,
                "Stable ?": stable,
            })

        return rows


    comparison = compare_methods(A_red, B_red, K_pp, K_oc)

    return (comparison,)


@app.cell
def _(comparison):
    import pandas as pd

    df_comparison = pd.DataFrame(comparison)
    df_comparison_rounded = df_comparison.copy()

    for col in ["Max |theta|", "Max |phi|", "|x(20)|", "|theta(20)|"]:
        df_comparison_rounded[col] = df_comparison_rounded[col].round(6)

    df_comparison_rounded
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Conclusions

    Les deux contrôleurs atteignent l’objectif demandé : ils stabilisent le booster et ramènent l’angle vers la position verticale.

    D’après les résultats numériques, on remarque que :

    - dans les deux cas, le maximum de $|\theta|$ vaut environ $0.785$, c’est-à-dire $\pi/4$, ce qui correspond simplement à l’angle initial ;
    - les deux contrôleurs gardent bien $|\theta| < \pi/2$ ;
    - les deux contrôleurs gardent aussi $|\phi| < \pi/2$ ;
    - les deux systèmes fermés sont asymptotiquement stables.

    Le placement de pôles donne une convergence légèrement meilleure en position finale :

    $$
    |x(20)| = 0.006201
    $$

    contre :

    $$
    |x(20)| = 0.008205
    $$

    pour le LQR.

    Cependant, le contrôleur LQR utilise une commande plus douce, car son maximum de commande est plus faible :

    $$
    \max |\phi| = 0.483678
    $$

    contre :

    $$
    \max |\phi| = 0.705351
    $$

    pour le placement de pôles.

    Donc, les deux méthodes fonctionnent, mais elles ont des comportements différents :

    - le placement de pôles est légèrement plus précis à la fin ;
    - le LQR est plus régulier et moins agressif en commande.

    Ainsi, si l’objectif principal est la précision finale, le placement de pôles est légèrement meilleur.
    Si l’objectif est de limiter l’effort de commande, le LQR est préférable.
    """)
    return


if __name__ == "__main__":
    app.run()
