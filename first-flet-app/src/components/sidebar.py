# coding: utf-8
import flet as ft
from utils import navigate_with_transition

def create_sidebar(page: ft.Page, current_page="home"):
    def navigate_to_main(e):
        from mainpage import mainpage
        new_content = mainpage(page, return_content=True)
        navigate_with_transition(page, new_content)

    def navigate_to_document_list(e):
        from document_list import document_list
        new_content = document_list(page, return_content=True)
        navigate_with_transition(page, new_content)

    def navigate_to_material_list(e):
        from material_list import material_list
        new_content = material_list(page, return_content=True)
        navigate_with_transition(page, new_content)

    def navigate_to_change_list(e):
        from change_list import change_list
        new_content = change_list(page, return_content=True)
        navigate_with_transition(page, new_content)

    def navigate_to_project_list(e):
        from project_list import project_list
        new_content = project_list(page, return_content=True)
        navigate_with_transition(page, new_content)

    def navigate_to_supplier_list(e):
        from supplier_list import supplier_list
        new_content = supplier_list(page, return_content=True)
        navigate_with_transition(page, new_content)

    def navigate_to_users(e):
        from users import users
        new_content = users(page, return_content=True)
        navigate_with_transition(page, new_content)

    def create_menu_item(text, icon, selected=False, on_click=None):
        return ft.Container(
            content=ft.Row(
                [
                    ft.Container(
                        content=ft.Icon(
                            icon,
                            color=ft.colors.BLUE_400 if selected else ft.colors.GREY_700,
                            size=24,
                        ),
                        width=40,
                        alignment=ft.alignment.center,
                    ),
                    ft.Container(
                        content=ft.Text(
                            text,
                            color=ft.colors.BLUE_400 if selected else ft.colors.GREY_700,
                            size=14,
                            selectable=True,
                        ),
                        width=120,
                    ),
                ],
                alignment=ft.MainAxisAlignment.START,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            padding=ft.padding.symmetric(horizontal=20, vertical=12),
            bgcolor=ft.colors.BLUE_50 if selected else None,
            border_radius=8,
            ink=True,
            on_click=on_click,
            height=48,
            width=200,
        )

    # 创建用户信息区域
    user_info = ft.Container(
        content=ft.Row(
            [
                ft.Container(
                    content=ft.CircleAvatar(
                        foreground_image_url="avatar.png",
                        radius=20,
                    ),
                    width=50,
                    alignment=ft.alignment.center,
                ),
                ft.Container(
                    content=ft.Column(
                        [
                            ft.Text("zzzyx", size=16, weight=ft.FontWeight.BOLD, selectable=True),
                            ft.Text("在线", size=12, color=ft.colors.GREY_700, selectable=True),
                        ],
                        spacing=2,
                        alignment=ft.MainAxisAlignment.CENTER,
                    ),
                    width=130,
                ),
            ],
            alignment=ft.MainAxisAlignment.START,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        padding=ft.padding.symmetric(horizontal=20, vertical=20),
        border=ft.border.only(bottom=ft.BorderSide(1, ft.colors.GREY_200)),
        height=80,
        width=200,
    )

    # 创建导航菜单
    nav_menu = ft.Column(
        [
            create_menu_item("首页", ft.icons.HOME, 
                selected=current_page=="home",
                on_click=navigate_to_main
            ),
            create_menu_item("文档管理", ft.icons.FOLDER, 
                selected=current_page=="documents",
                on_click=navigate_to_document_list
            ),
            create_menu_item("物料管理", ft.icons.INVENTORY, 
                selected=current_page=="materials",
                on_click=navigate_to_material_list
            ),
            create_menu_item("变更管理", ft.icons.COMPARE_ARROWS, 
                selected=current_page=="changes",
                on_click=navigate_to_change_list
            ),
            create_menu_item("项目管理", ft.icons.BUSINESS_CENTER, 
                selected=current_page=="projects",
                on_click=navigate_to_project_list
            ),
            create_menu_item("供应商管理", ft.icons.STORE, 
                selected=current_page=="suppliers",
                on_click=navigate_to_supplier_list
            ),
            create_menu_item("用户管理", ft.icons.PERSON, 
                selected=current_page=="users",
                on_click=navigate_to_users
            ),
        ],
        spacing=1,
        scroll=ft.ScrollMode.AUTO,
    )

    # 创建侧边栏容器
    return ft.Container(
        content=ft.Column(
            [
                user_info,
                ft.Container(
                    content=nav_menu,
                    expand=True,
                    padding=ft.padding.only(top=10),
                ),
            ],
            spacing=0,
        ),
        width=200,
        height=page.window_height,
        bgcolor=ft.colors.WHITE,
        border=ft.border.only(right=ft.BorderSide(1, ft.colors.GREY_200)),
    ) 