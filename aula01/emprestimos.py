import datetime

# Variáveis globais acessadas diretamente pela classe
equipamentos = [
    {"id": 1, "nome": "Notebook Dell",  "tipo": "notebook", "disponivel": True},
    {"id": 2, "nome": "Projetor Epson", "tipo": "projetor",  "disponivel": True},
    {"id": 3, "nome": "Cabo HDMI",      "tipo": "cabo",      "disponivel": True},
]
emprestimos_registrados = []


class Sistema:

    def registrar(self, equipamento_id, usuario_nome, usuario_email, dias):
        equipamento = None
        for e in equipamentos:           # acessa variável global diretamente
            if e["id"] == equipamento_id:
                equipamento = e
                break

        if equipamento is None or not equipamento["disponivel"]:
            print("Equipamento inválido ou indisponível")
            return False

        data_emprestimo = datetime.date.today()
        data_devolucao  = data_emprestimo + datetime.timedelta(days=dias)

        emprestimo = {
            "id":               len(emprestimos_registrados) + 1,
            "equipamento_id":   equipamento_id,
            "equipamento_nome": equipamento["nome"],
            "tipo":             equipamento["tipo"],
            "usuario_nome":     usuario_nome,
            "usuario_email":    usuario_email,
            "data_emprestimo":  data_emprestimo,
            "data_devolucao":   data_devolucao,
            "devolvido":        False,
        }
        emprestimos_registrados.append(emprestimo)
        equipamento["disponivel"] = False

        # notificação misturada com lógica de negócio
        print(f"[EMAIL] {usuario_email} — empréstimo até {data_devolucao}")
        return True

    def devolver(self, emprestimo_id):
        emprestimo = None
        for e in emprestimos_registrados:
            if e["id"] == emprestimo_id:
                emprestimo = e
                break

        if emprestimo is None or emprestimo["devolvido"]:
            print("Empréstimo inválido ou já devolvido")
            return

        emprestimo["devolvido"] = True
        hoje   = datetime.date.today()
        atraso = (hoje - emprestimo["data_devolucao"]).days

        # cálculo de multa com if/elif — violação de OCP
        multa = 0
        if atraso > 0:
            if emprestimo["tipo"] == "notebook":
                multa = atraso * 10.0
            elif emprestimo["tipo"] == "projetor":
                multa = atraso * 15.0
            elif emprestimo["tipo"] == "cabo":
                multa = atraso * 2.0

        for e in equipamentos:
            if e["id"] == emprestimo["equipamento_id"]:
                e["disponivel"] = True

        # notificação misturada aqui também
        print(f"[EMAIL] {emprestimo['usuario_email']} — multa R${multa:.2f}")
        print(f"Devolução registrada. Multa: R${multa:.2f}")

    def listar_atrasados(self):
        hoje = datetime.date.today()
        for e in emprestimos_registrados:
            if not e["devolvido"] and e["data_devolucao"] < hoje:
                atraso = (hoje - e["data_devolucao"]).days

                # cálculo de multa duplicado — violação de DRY
                multa = 0
                if e["tipo"] == "notebook":
                    multa = atraso * 10.0
                elif e["tipo"] == "projetor":
                    multa = atraso * 15.0
                elif e["tipo"] == "cabo":
                    multa = atraso * 2.0

                print(f"{e['usuario_nome']} — {atraso} dias — R${multa:.2f}")

                # notificação pela terceira vez no sistema
                print(f"[EMAIL] {e['usuario_email']} — você está em atraso!")


# menu misturado no mesmo arquivo com a lógica de negócio
def main():
    s = Sistema()
    while True:
        print("\n1-Registrar  2-Devolver  3-Atrasados  0-Sair")
        op = input("Opção: ")
        if op == "1":
            s.registrar(
                int(input("ID equipamento: ")),
                input("Nome: "),
                input("Email: "),
                int(input("Dias: "))
            )
        elif op == "2":
            s.devolver(int(input("ID empréstimo: ")))
        elif op == "3":
            s.listar_atrasados()
        elif op == "0":
            break


if __name__ == "__main__":
    main()
