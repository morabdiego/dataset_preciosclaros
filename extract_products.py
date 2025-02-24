import pandas as pd

# Define dtypes for productos
productos_dtypes = {
    'id_comercio': 'string',
    'id_bandera': 'float32',
    'id_sucursal': 'float32',
    'id_producto': 'float32',
    'productos_ean': 'float32',
    'productos_descripcion': 'string',
    'productos_cantidad_presentacion': 'float32',
    'productos_unidad_medida_presentacion': 'string',
    'productos_marca': 'string',
    'productos_precio_lista': 'float32',
    'productos_precio_referencia': 'float32',
    'productos_cantidad_referencia': 'float32',
    'productos_unidad_medida_referencia': 'string',
    'productos_precio_unitario_promo1': 'float32',
    'productos_leyenda_promo1': 'string',
    'productos_precio_unitario_promo2': 'float32',
    'productos_leyenda_promo2': 'string'
}

# Read CSV with optimized dtypes
productos = pd.read_csv(
    './data/data_productos.csv', 
    sep='|',
    dtype=productos_dtypes,
    low_memory=False
)

# Export unique product descriptions
productos['productos_descripcion'].value_counts().to_excel('./data/productos_unique.xlsx')