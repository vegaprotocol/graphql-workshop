import click
import json
from gql import gql, Client
from gql.transport.aiohttp import AIOHTTPTransport


@click.group()
def cli():
    pass


@cli.command()
def stats():
    click.echo('Loading statistics from Vega GraphQL API')
    # todo: Implement loading of statistics


@cli.command()
@click.option('--pubkey', default='', help='address of party on Vega [pub-key]')
def orders(pubkey):
    click.echo('Loading orders from Vega GraphQL API ' + pubkey)
    # todo: Implement loading orders with optional party


@cli.command()
def parties():
    query = gql(
        """
        query {
          parties{
            id
          }
        }
        """
    )
    click.echo('Querying parties from Vega GraphQL API')
    result = perform_query(query)
    echo_result(result)


def perform_query(query):
    transport = AIOHTTPTransport(url="https://lb.testnet.vega.xyz/query")
    client = Client(transport=transport, fetch_schema_from_transport=True)
    result = client.execute(query)
    return result


def echo_result(result):
    click.echo(json.dumps(result, indent=2, sort_keys=True))


if __name__ == '__main__':
    cli()