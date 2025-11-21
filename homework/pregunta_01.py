# pylint: disable=line-too-long
"""
Escriba el codigo que ejecute la accion solicitada.
"""


def pregunta_01():
    """
    El archivo `files//shipping-data.csv` contiene información sobre los envios
    de productos de una empresa. Cree un dashboard estático en HTML que
    permita visualizar los siguientes campos:

    * `Warehouse_block`

    * `Mode_of_Shipment`

    * `Customer_rating`

    * `Weight_in_gms`

    El dashboard generado debe ser similar a este:

    https://github.com/jdvelasq/LAB_matplotlib_dashboard/blob/main/shipping-dashboard-example.png

    Para ello, siga las instrucciones dadas en el siguiente video:

    https://youtu.be/AgbWALiAGVo

    Tenga en cuenta los siguientes cambios respecto al video:

    * El archivo de datos se encuentra en la carpeta `data`.

    * Todos los archivos debe ser creados en la carpeta `docs`.

    * Su código debe crear la carpeta `docs` si no existe.

    """
    import os
    import pandas as pd
    import matplotlib.pyplot as plt

    # Ensure output directory exists
    outdir = "docs"
    os.makedirs(outdir, exist_ok=True)

    # Read the data
    csv_path = os.path.join("files", "input", "shipping-data.csv")
    df = pd.read_csv(csv_path)

    # 1) Shipping per warehouse (counts)
    fig, ax = plt.subplots(figsize=(6, 4))
    counts = df['Warehouse_block'].value_counts().sort_index()
    counts.plot(kind='bar', color='tab:blue', ax=ax)
    ax.set_title('Shipments per Warehouse')
    ax.set_xlabel('Warehouse_block')
    ax.set_ylabel('Number of shipments')
    plt.tight_layout()
    fig.savefig(os.path.join(outdir, 'shipping_per_warehouse.png'))
    plt.close(fig)

    # 2) Mode of shipment (counts)
    fig, ax = plt.subplots(figsize=(6, 4))
    mode_counts = df['Mode_of_Shipment'].value_counts()
    mode_counts.plot(kind='bar', color='tab:green', ax=ax)
    ax.set_title('Mode of Shipment')
    ax.set_xlabel('Mode_of_Shipment')
    ax.set_ylabel('Number of shipments')
    plt.tight_layout()
    fig.savefig(os.path.join(outdir, 'mode_of_shipment.png'))
    plt.close(fig)

    # 3) Average customer rating per warehouse
    fig, ax = plt.subplots(figsize=(6, 4))
    avg_rating = df.groupby('Warehouse_block')['Customer_rating'].mean().sort_index()
    avg_rating.plot(kind='bar', color='tab:orange', ax=ax)
    ax.set_title('Average Customer Rating by Warehouse')
    ax.set_xlabel('Warehouse_block')
    ax.set_ylabel('Average Customer Rating')
    plt.tight_layout()
    fig.savefig(os.path.join(outdir, 'average_customer_rating.png'))
    plt.close(fig)

    # 4) Weight distribution histogram
    fig, ax = plt.subplots(figsize=(6, 4))
    df['Weight_in_gms'].plot(kind='hist', bins=30, color='tab:purple', ax=ax)
    ax.set_title('Weight Distribution (gms)')
    ax.set_xlabel('Weight_in_gms')
    ax.set_ylabel('Frequency')
    plt.tight_layout()
    fig.savefig(os.path.join(outdir, 'weight_distribution.png'))
    plt.close(fig)

    # Create a simple index.html embedding the images
    html_path = os.path.join(outdir, 'index.html')
    with open(html_path, 'w', encoding='utf-8') as fh:
        fh.write('<!doctype html>\n')
        fh.write('<html><head><meta charset="utf-8"><title>Shipping Dashboard</title></head><body>\n')
        fh.write('<h1>Shipping Dashboard</h1>\n')
        fh.write('<h2>Shipments per Warehouse</h2>\n')
        fh.write('<img src="shipping_per_warehouse.png" alt="shipping_per_warehouse" style="max-width:100%">\n')
        fh.write('<h2>Mode of Shipment</h2>\n')
        fh.write('<img src="mode_of_shipment.png" alt="mode_of_shipment" style="max-width:100%">\n')
        fh.write('<h2>Average Customer Rating</h2>\n')
        fh.write('<img src="average_customer_rating.png" alt="average_customer_rating" style="max-width:100%">\n')
        fh.write('<h2>Weight Distribution</h2>\n')
        fh.write('<img src="weight_distribution.png" alt="weight_distribution" style="max-width:100%">\n')
        fh.write('</body></html>\n')

    return None
