{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "087f809a-274a-414c-a5ca-5b343b6061e8",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " * Serving Flask app '__main__'\n",
      " * Debug mode: on\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.\n",
      " * Running on http://127.0.0.1:5000\n",
      "Press CTRL+C to quit\n",
      " * Restarting with watchdog (windowsapi)\n"
     ]
    },
    {
     "ename": "SystemExit",
     "evalue": "1",
     "output_type": "error",
     "traceback": [
      "An exception has occurred, use %tb to see the full traceback.\n",
      "\u001b[1;31mSystemExit\u001b[0m\u001b[1;31m:\u001b[0m 1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "D:\\Programas\\Anaconda\\Lib\\site-packages\\IPython\\core\\interactiveshell.py:3585: UserWarning: To exit: use 'exit', 'quit', or Ctrl-D.\n",
      "  warn(\"To exit: use 'exit', 'quit', or Ctrl-D.\", stacklevel=1)\n"
     ]
    }
   ],
   "source": [
    "from flask import Flask, request, jsonify\n",
    "import pandas as pd\n",
    "from sklearn.linear_model import LinearRegression\n",
    "import joblib\n",
    "import os\n",
    "\n",
    "app = Flask(__name__)\n",
    "\n",
    "# Ruta al archivo CSV y al archivo del modelo\n",
    "#ruta='D:/2. Proyectos/3. Python/3.-Laboratorio/dataset.xlsx'\n",
    "#ruta_csv = 'ruta/al/archivo/cotizaciones.csv'\n",
    "ruta_csv = 'D:/2. Proyectos/3. Python/3.-Laboratorio/dataset.csv'\n",
    "ruta_modelo = 'modelo_entrenado.pkl'\n",
    "\n",
    "# Entrenar el modelo y guardarlo en un archivo si no existe\n",
    "def entrenar_modelo(ruta_csv, ruta_modelo):\n",
    "    if not os.path.exists(ruta_modelo):\n",
    "        # Leer el archivo CSV con el separador correcto\n",
    "        df = pd.read_csv(ruta_csv, sep=';')  # Cambia sep=',' si tu CSV usa otro separador como ';' o '\\t'\n",
    "        # Definir las características (X) y la variable objetivo (y)\n",
    "        X = df[['Open', 'High', 'Low','Volume']]\n",
    "        y = df['Adj Close']\n",
    "        model = LinearRegression()\n",
    "        model.fit(X, y)\n",
    "        joblib.dump(model, ruta_modelo)\n",
    "\n",
    "# Entrenar el modelo y guardarlo si es necesario\n",
    "entrenar_modelo(ruta_csv, ruta_modelo)\n",
    "\n",
    "# Cargar el modelo entrenado\n",
    "modelo = joblib.load(ruta_modelo)\n",
    "\n",
    "@app.route('/predict', methods=['POST'])\n",
    "def predecir_precio():\n",
    "    data = request.get_json()\n",
    "    open_price = data['Open']\n",
    "    high_price = data['High']\n",
    "    low_price = data['Low']\n",
    "    volume = data['Volume']\n",
    "\n",
    "    datos_entrada = pd.DataFrame({\n",
    "        'Open': [open_price],\n",
    "        'High': [high_price],\n",
    "        'Low': [low_price],\n",
    "        'Volume': [volume]\n",
    "    })\n",
    "\n",
    "    prediccion = modelo.predict(datos_entrada)\n",
    "    return jsonify({'prediccion': prediccion[0]})\n",
    "\n",
    "if __name__ == '__main__':\n",
    "    app.run(debug=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "991a551a-bc03-4976-b204-f9195382cf93",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
