import click

# Ruta al archivo de contactos
CONTACTS_FILE = "contacts.txt"

@click.command()
def create_contact():
    """Crear un nuevo contacto."""
    first_name = click.prompt("Nombre")
    last_name = click.prompt("Apellido")
    email = click.prompt("Email")
    phone = click.prompt("Teléfono")

    with open(CONTACTS_FILE, "a") as file:
        file.write(f"{first_name} - {last_name} - {email} - {phone}\n")
    
    click.echo("Contacto creado con éxito.")

@click.command()
def list_contacts():
    """Listar todos los contactos."""
    with open(CONTACTS_FILE, "r") as file:
        contacts = file.readlines()
    
    if contacts:
        click.echo("Lista de contactos:")
        for contact in contacts:
            click.echo(contact.strip())
    else:
        click.echo("No hay contactos registrados.")

@click.command()
@click.argument("query")
def search_contact(query):
    """Buscar contactos por nombre o email."""
    with open(CONTACTS_FILE, "r") as file:
        contacts = file.readlines()

    matching_contacts = [contact for contact in contacts if query in contact]

    if matching_contacts:
        click.echo("Resultados de búsqueda:")
        for contact in matching_contacts:
            click.echo(contact.strip())
    else:
        click.echo("No se encontraron contactos que coincidan con la búsqueda.")

@click.group()
def main():
    pass

main.add_command(create_contact)
main.add_command(list_contacts)
main.add_command(search_contact)

if __name__ == '__main__':
    main()
