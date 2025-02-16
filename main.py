from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt

console = Console()

class Person:
    def __init__(self, id, name, partner=None):
        self.id = id
        self.name = name
        self.partner = partner
        self.children = []

    def add_child(self, child):
        self.children.append(child)

class FamilyTree:
    def __init__(self):
        self.people = {}

    def add_person(self, id, name, partner_id=None):
        person = Person(id, name)
        self.people[id] = person
        if partner_id and partner_id in self.people:
            partner = self.people[partner_id]
            person.partner = partner
            partner.partner = person

    def remove_person(self, id):
        if id in self.people:
            if self.people[id].partner:
                self.people[id].partner.partner = None
            del self.people[id]

    def modify_partner(self, id, partner_id):
        if id in self.people and partner_id in self.people:
            self.people[id].partner = self.people[partner_id]
            self.people[partner_id].partner = self.people[id]

    def add_child(self, parent_id, child_id):
        if parent_id in self.people and child_id in self.people:
            self.people[parent_id].add_child(self.people[child_id])

    def remove_child(self, parent_id, child_id):
        if parent_id in self.people and child_id in self.people:
            self.people[parent_id].children = [
                child for child in self.people[parent_id].children if child.id != child_id
            ]

    def print_tree(self):
        console.print("[bold cyan]--- Árbol Genealógico ---[/bold cyan]", style="bold yellow")
        for id, person in self.people.items():
            partner_name = person.partner.name if person.partner else "Ninguna"
            console.print(f"[bold green]{person.name}[/bold green] (ID: {id})")
            console.print(f"  Pareja: [bold red]{partner_name}[/bold red]")
            for child in person.children:
                console.print(f"    Hijo: [bold blue]{child.name}[/bold blue] (ID: {child.id})")

def show_menu():
    while True:
        console.print(Panel.fit(
            "[1] [green]Añadir Persona[/green]\n"
            "[2] [green]Eliminar Persona[/green]\n"
            "[3] [green]Modificar Pareja[/green]\n"
            "[4] [green]Añadir Hijo[/green]\n"
            "[5] [green]Eliminar Hijo[/green]\n"
            "[6] [green]Imprimir Árbol[/green]\n"
            "[7] [red]Salir[/red]",
            title="Menú Árbol Genealógico",
            border_style="bold cyan"
        ))
        option = Prompt.ask("[bold yellow]Elige una opción[/bold yellow]", choices=["1", "2", "3", "4", "5", "6", "7"])

        if option == "1":
            id = int(Prompt.ask("ID de la Persona"))
            name = Prompt.ask("Nombre de la Persona")
            partner_id = Prompt.ask("ID de la Pareja (opcional)", default=None)
            tree.add_person(id, name, int(partner_id) if partner_id else None)
        elif option == "2":
            id = int(Prompt.ask("ID de la Persona a eliminar"))
            tree.remove_person(id)
        elif option == "3":
            id = int(Prompt.ask("ID de la Persona"))
            partner_id = int(Prompt.ask("ID de la nueva Pareja"))
            tree.modify_partner(id, partner_id)
        elif option == "4":
            parent_id = int(Prompt.ask("ID del Padre o Madre"))
            child_id = int(Prompt.ask("ID del Hijo"))
            tree.add_child(parent_id, child_id)
        elif option == "5":
            parent_id = int(Prompt.ask("ID del Padre o Madre"))
            child_id = int(Prompt.ask("ID del Hijo a eliminar"))
            tree.remove_child(parent_id, child_id)
        elif option == "6":
            tree.print_tree()
        elif option == "7":
            console.print("[bold red]Saliendo...[/bold red]")
            break
        
tree = FamilyTree()
show_menu()
