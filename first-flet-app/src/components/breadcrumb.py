# coding: utf-8
import flet as ft
from utils import navigate_with_transition

def create_breadcrumb(page: ft.Page, items: list):
    """
    创建面包屑导航
    :param page: 页面对象
    :param items: 面包屑项列表，每项为字典，包含 text 和 on_click 两个键
    """
    breadcrumb_items = []
    
    for i, item in enumerate(items):
        # 添加面包屑项
        breadcrumb_items.append(
            ft.TextButton(
                text=item["text"],
                style=ft.ButtonStyle(
                    color=ft.colors.BLUE_400 if i == len(items) - 1 else ft.colors.GREY_700,
                    padding=ft.padding.all(0),
                ),
                on_click=item.get("on_click"),
            )
        )
        
        # 添加分隔符，最后一项不添加
        if i < len(items) - 1:
            breadcrumb_items.append(
                ft.Text(
                    "/",
                    size=14,
                    color=ft.colors.GREY_400,
                    weight=ft.FontWeight.BOLD,
                )
            )
    
    return ft.Container(
        content=ft.Row(
            breadcrumb_items,
            spacing=8,
            alignment=ft.MainAxisAlignment.START,
        ),
        padding=ft.padding.only(left=20, top=16, bottom=16),
        bgcolor=ft.colors.WHITE,
        border=ft.border.only(bottom=ft.BorderSide(1, ft.colors.GREY_200)),
    ) 