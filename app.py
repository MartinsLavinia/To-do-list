from flask import Flask, render_template, request, redirect, flash
from conexao import criar_nota, listar_notas, buscar_nota, update_nota, excluir_nota

app = Flask(__name__)
app.secret_key = "bloco_de_notas"


@app.route("/")
def home():

    notas = listar_notas()

    return render_template("index.html", notas=notas)


@app.route("/nova-nota", methods=["GET", "POST"])
def nova_nota():

    if request.method == "POST":

        titulo = request.form["titulo"]
        conteudo = request.form["conteudo"]

        criar_nota(titulo, conteudo)

        flash("✅ Nota salva com sucesso!", "sucesso")
        return redirect("/")

    return render_template("nova_nota.html")


@app.route("/editar-nota/<int:id>", methods=["GET", "POST"])
def editar_nota(id):

    if request.method == "POST":

        titulo = request.form["titulo"]
        conteudo = request.form["conteudo"]

        update_nota(id, titulo, conteudo)

        flash("✏️ Nota atualizada com sucesso!", "sucesso")
        return redirect("/")

    nota = buscar_nota(id)

    return render_template("editar_nota.html", nota=nota)


@app.route("/excluir-nota/<int:id>")
def deletar_nota(id):

    excluir_nota(id)

    flash("🗑️ Nota excluída com sucesso!", "excluir")

    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)