import marimo

__generated_with = "0.11.25"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo

    mo.md("# Hello\n# World")
    return (mo,)


@app.cell
def _(mo):
    mo.md(
        r"""
        Markdown Text
        ---
        - line 1
        - line 2
        - line 3
        """
    )
    return


@app.cell
def _():
    x = 10
    return (x,)


@app.cell
def _(x):
    y = x * 10
    y
    return (y,)


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
