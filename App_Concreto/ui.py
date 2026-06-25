import flet as ft
from App_Concreto.calculos import calcular_volume, calcular_materiais

def main(page: ft.Page):
    page.title = "Calculadora de Concreto Civil"
    page.theme_mode = ft.ThemeMode.LIGHT

    # Cabeçalho
    titulo = ft.Text(
        "🏗️ Calculadora de Concreto Civil",
        size=24,
        weight=ft.FontWeight.BOLD,
        color=ft.Colors.BLUE_900
    )
    subtitulo = ft.Text(
        "Informe as dimensões e o tipo de elemento estrutural",
        size=16,
        color=ft.Colors.BLUE_600
    )

    # Campos de entrada
    largura = ft.TextField(label="Largura (m)", width=150)
    altura = ft.TextField(label="Altura (m)", width=150)
    comprimento = ft.TextField(label="Comprimento (m)", width=150)

    tipo = ft.Dropdown(
        label="Tipo de elemento",
        options=[
            ft.dropdown.Option("viga_pilar"),
            ft.dropdown.Option("baldrame"),
            ft.dropdown.Option("laje_25"),
            ft.dropdown.Option("laje_30"),
        ],
        width=200
    )

    # Resultado
    resultado = ft.Text("", size=16, color=ft.Colors.BLACK)

    # Função de cálculo
    def calcular(e):
        try:
            vol = calcular_volume(float(largura.value), float(altura.value), float(comprimento.value))
            materiais = calcular_materiais(tipo.value, vol)
            resultado.value = (
                f"📐 Volume total: {materiais['volume_total']} m³\n"
                f"🏗️ Fck: {materiais['fck']} MPa\n"
                f"🧱 Cimento: {materiais['cimento']} sacos\n"
                f"🏖️ Areia: {materiais['areia']} m³\n"
                f"🪨 Brita: {materiais['brita']} m³"
            )
            page.update()
        except Exception as ex:
            resultado.value = f"Erro: {ex}"
            page.update()

    # Botão
    btn_calcular = ft.ElevatedButton(
        "Calcular",
        bgcolor=ft.Colors.GREEN_600,
        color=ft.Colors.WHITE,
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=10),
            padding=20
        ),
        on_click=calcular
    )

    # Layout organizado
    page.add(
    titulo,
    subtitulo,
    ft.Row([largura, altura, comprimento], alignment=ft.MainAxisAlignment.CENTER),
    tipo,
    btn_calcular,
    ft.Container(
        resultado,
        padding=20,
        border=ft.Border.all(1, ft.Colors.GREY),
        border_radius=10
    )
)
