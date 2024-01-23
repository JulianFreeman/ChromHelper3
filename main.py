# coding: utf8
import flet as ft

from utils import ExtensionsData, scan_extensions

extensions_data: ExtensionsData = scan_extensions()


def main(page: ft.Page):
    page.theme_mode = ft.ThemeMode.LIGHT

    sd = ft.Column(
        # width=200,
        controls=[
            ft.Text("ChromHelper3", size=20)
        ],
        # alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )

    cl = ft.Column(
        controls=[
            ft.Container(
                content=ft.ListTile(
                    leading=ft.Image(src=extensions_data[eid].icon),
                    title=ft.Text(extensions_data[eid].name),
                    trailing=ft.ElevatedButton("Click", style=ft.ButtonStyle(
                        shape=ft.RoundedRectangleBorder(radius=4)
                    )),
                ),
                # content=ft.Text("Helo"),
                bgcolor=ft.colors.GREEN_50,
                border_radius=6,
            )
            for eid in extensions_data

        ],
        scroll=ft.ScrollMode.ALWAYS,
        # expand=True,
    )

    page.add(ft.Row(
        controls=[
            ft.Container(
                content=sd, bgcolor=ft.colors.GREY_200, border_radius=10,
                width=200,
            ),
            ft.Container(
                content=cl, bgcolor=ft.colors.GREY_100, expand=True,
                alignment=ft.alignment.top_center,
            )
        ],
        # alignment=ft.MainAxisAlignment.START,
        expand=True
    ))
    # page.add(cl)


ft.app(target=main)
