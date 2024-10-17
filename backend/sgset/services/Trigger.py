import os
from DataDownloader import load_configurations, pipeline_step

def main():
    """Main function to load configurations and execute the scraping pipeline.
    """
    config = load_configurations('../../config.yaml')

    config['download_folder'] = os.path.join(os.path.expanduser("~"), "Downloads")

    pipeline_step(
        config['url'],
        config['edge_driver_path'],
        config['destination_folder'],
        config['download_folder'],
        config['timeout']
    )

if __name__ == "__main__":
    main()
