
import click, subprocess


def login_to_ccloud():
    subprocess.run(['ccloud', 'login'])


class CCLoudKsqlDB:
    def create_ksql_app(self, name):
        """ Create a new ksqldb app

        Args:
            name: str, the name of the ksqldb app
        """
        subprocess.run(['ccloud', 'ksql', 'app', 'create', name])

    def delete_ksql_app(self, id):
        """ Delete a new ksqldb app

        Args:
            name: str, the name of the ksqldb app
        """
        subprocess.run(['ccloud', 'ksql', 'app', 'delete', id])

    def describe_ksql_app(self, id):
        """ Describe an exiting ksqldb app

        Args:
            id: str, the id of the ccloud ksqldb
        """
        subprocess.run(['ccloud', 'ksql', 'app', 'describe', id])

    def list_ksql_apps(self,):
        """ List ksqldb apps"""
        subprocess.run(['ccloud', 'ksql', 'app', 'list'])


class CCLoudConnector:

    def create_connector_app(self, cluster, config):
        """ Create a new connector app

        Args:
            cluster: str, the id of the ccloud cluster
            config: str, the path to the config
        """
        subprocess.run(['ccloud', 'connector', 'create', '--cluster', cluster, '--config', config])

    def delete_connector_app(self, id):
        """ Delete a connector app
        Args:
            id: str, the id of the ccloud connector
        """
        print("Deleting the connector...")
        subprocess.run(['ccloud', 'connector',  'delete', id])

    def describe_connector_app(self, id):
        """ Describe an existing connector app

        Args:
            id: str, the id of the ccloud connector
        """
        subprocess.run(['ccloud', 'connector',  'describe', id])

    def list_connector_apps(self,):
        """ List the connector apps
        """
        subprocess.run(['ccloud', 'connector', 'list'])


class CCLoudServiceAccount:

    def create_service_account(self, name):
        """ Create a new service account

        Args:
            name: str, the name of the service account
        """
        subprocess.run(['ccloud', 'service-account', 'create', name])

    def delete_service_account(self, id):
        """ Delete a service account

        Args:
           id: str, the id of the ccloud service account
        """
        subprocess.run(['ccloud', 'service-account',  'delete', id])

    def update_service_account(self, id, description):
        """ Update the description of an existing service account

        Args:
            id: str, the id of the ccloud service account
            description: str, the description of the ccloud service account
        """
        subprocess.run(['ccloud', 'service-account',  'update', id, description])

    def list_service_accounts(self,):
        """ List the service accounts
        """
        subprocess.run(['ccloud', 'service-account', 'list'])

class CCLoudApiKey:

    def create_api_key(self, resource,  service_account, description, output, environment):
        """ Create a new api key

        Args:
            name: str, the name of the api key
        """
        subprocess.run(['ccloud', 'api-key', 'create', resource, service_account, description, output, environment])

    def delete_api_key(self, api_key):
        """ Delete a api key

        Args:
           api_key: str, the ccloud api_key you wish to delete. It will delete the api secret as well
        """
        subprocess.run(['ccloud', 'api-key',  'delete', api_key])

    def update_api_key(self, api_key, description):
        """ Update the description of an existing api key

        Args:
            api_key: str, the ccloud api_key you wish to update
            description: str, the description of the ccloud api key
        """
        subprocess.run(['ccloud', 'api-key',  'update', api_key, '--description', description])

    def store_api_key(self, api_key):
        """ Describe an existing connector app

        Args:
            api_key: str, the ccloud api_key
        """
        subprocess.run(['ccloud', 'api-key',  'store', api_key])

    def list_api_keys(self,):
        """ List all the api keys in your environment
        """
        subprocess.run(['ccloud', 'api-key', 'list'])

    def use_api_keys(self, api_key, id):
        """ List all the api keys in your environment
        """
        subprocess.run(['ccloud', 'api-key', 'use', api_key, '--resource', id])


supported_components = {
    'ksql': {
        'class': CCLoudKsqlDB(),
    },
    'connector': {
        'class': CCLoudConnector(),
    },
    'service_account': {
        'class': CCLoudServiceAccount(),
    },

    'api_key': {
        'class': CCLoudApiKey(),
    }
}


supported_actions = (
    'create',
    'delete',
    'describe',
    'list',
    'update',
    'use',
    'store'
)


@click.command()
@click.argument('component', type=click.Choice(supported_components.keys()))
@click.argument('action', type=click.Choice(supported_actions))
@click.option('--config',  help='The path to the connector config file ')
@click.option('--cluster',   help='The id of the cluster')
@click.option('--description',   help='The description of the service account')
@click.option('--id',   help='The id of the kafka component')
@click.option('--name',  help='The name of the ksql db app or service account')
@click.option('--environment',  help='The name of the environment')
@click.option('--serv_acct',   help='The service account that an api-key is added to')
@click.option('--api_key',  help='The name of the api key')
def main(component, action, config, cluster, description, id, name, serv_acct, output, environment, api_key):
    login_to_ccloud()
    if component == 'connector':
        if action == 'create':
            getattr(supported_components[component]['class'],
                    f'{action}_{component}_app')(cluster, config)
        elif action == 'describe' or action == 'delete':
            getattr(supported_components[component]['class'],
                    f'{action}_{component}_app')(id)
        else:
            getattr(supported_components[component]['class'],
                    f'{action}_{component}_apps')()

    elif component == 'ksql':
        if action == 'create':
            getattr(supported_components[component]['class'],
                    f'{action}_{component}_app')(name)
        elif action == 'describe' or action == 'delete':
            getattr(supported_components[component]['class'],
                    f'{action}_{component}_app')(id)
        else:
            getattr(supported_components[component]['class'],
                    f'{action}_{component}_apps')()

    elif component == 'api_key':
        if action == 'create':
            getattr(supported_components[component]['class'],
                    f'{action}_{component}')(id, serv_acct, id, output, environment)
        elif action == 'delete':
            getattr(supported_components[component]['class'],
                    f'{action}_{component}')(api_key)
        elif action == 'update':
            getattr(supported_components[component]['class'],
                    f'{action}_{component}')(id, description)
        else:
            getattr(supported_components[component]['class'],
                    f'{action}_{component}s')()
    else:
        if action == 'create':
            getattr(supported_components[component]['class'],
                    f'{action}_{component}')(name)
        elif action == 'delete':
            getattr(supported_components[component]['class'],
                    f'{action}_{component}')(id)
        elif action == 'update':
            getattr(supported_components[component]['class'],
                    f'{action}_{component}')(id, description)
        else:
            getattr(supported_components[component]['class'],
                    f'{action}_{component}s')()


if __name__ == '__main__':
    main()
