#importación de librerias base
import pandas as pd

#Función que permite verificar la existencia de datos NaN, o de otro tipo según el parámetro que se ingrese
def cuenta_nan(df, dato_nan=""):
	"""Imprime el listado de variables con datos considerados como NaN.
	Parametros:
		df(df): DataFrame
		dato_nan(str): String correspondiente al dato que se considera NaN
	Retorno:
		Imprime el listado de variables con datos considerados NaN
	"""
	for i in df.columns:
		if dato_nan!="":
			if str(dato_nan) in df[i].unique():
				print(f"La variable \033[1m{i} contiene {len(df[df[i] == str(dato_nan)])} '{dato_nan}'\033[0m")
			else:
				print(f"La variable {i} no contiene '{dato_nan}'")
		else:
			if True in df[i].isna().unique():
				print(f"La variable \033[1m{i} contiene {df[i].isna().value_counts()[True]} 'NaN'\033[0m")
			else:
				print(f"La variable {i} no contiene 'NaN'")


#Función que genera gráficos de la variables acorde a tipo de datos que contienen.
#Librerías para la visualización de gráficos
import seaborn as sns
import matplotlib.pyplot as plt
def graficar_variables (df, curva=True):
	"""Genera gráficos de la variables acorde a tipo de datos que contienen.
	Parametros:
		df(df): DataFrame
	Retorno:
		Genera gráficos de la variables acorde a tipo de datos que contienen.
	"""
	for n, i in enumerate(df):
		# plt.subplot((len(list(df.columns))/2)+1,2,n+1)
		plt.subplot((len(list(df.columns)))+1,1,n+1)
		#la variable es continua (contiene número reales)
		titulo = str(f"Histograma de la variable '{i}'")
		texto_ejex = str(f"Valores de la variable '{i}'")
		if df[i].dtypes ==float:
			sns.distplot(df[i], kde=curva)
			plt.title(titulo, weight='bold')
			plt.xlabel(texto_ejex)
		#la variable es categórica
		elif df[i].dtypes =="object":
			sns.countplot(df[i])
			plt.title(titulo, weight='bold')
			plt.xlabel(texto_ejex)
		#la variable es discreta (contiene número enteros)
		else:
			sns.distplot(df[i],kde!=curva, bins=20)
			plt.title(titulo, weight='bold')
			plt.xlabel(texto_ejex)
	plt.tight_layout(h_pad=5)


#Función que genera gráficos tipo boxplot sobre el DataFrame
#creada originalmente por Wilson
def df_boxplot (df):
	"""Genera gráficos tipo boxplot sobre el DataFrame. Desarrollada por Wilson
	Parametros:
		df(df): DataFrame
	Retorno:
		Genera gráficos tipo boxplot sobre las variables del DataFrame.
	"""
	categorica=[]
	numerica=[]
	for n, i in enumerate(df):
		if (df[i].dtypes =="object"):
			categorica.append(i)
		else:
			numerica.append(i)
	print("Las variables numericas son {}".format(numerica))
	print("Las variables cateroricas son {}".format(categorica))

	n=1
	for i in categorica:
		for j in numerica:
			plt.subplot((len(list(df.columns))/3)+2,3,n)
			ax=sns.boxplot(x=i, y=j ,data=df)
			n+=1
	plt.tight_layout()

#Función que binariza variables categóricas
def binarizador (df):
	"""Binariza el dataframe ingresado
	Parametros:
		df(df): DataFrame
	Retorno:
		Devuelve un df binarizado
	"""
	#declaramos un df vacio a utilizar
	df_binarizado = pd.DataFrame()

	#obtenemos una lista de las variables categóricas
	variables_categoricas = list(df.select_dtypes(object).columns)

	#binarizamos las variables categóricas
	df_binarizado=pd.get_dummies(data=df, columns=variables_categoricas,drop_first=True)

	#reemplazamos el caracter '-' por '_' en los nombres de las variables
	#para evitar problemas futuros en el modelamiento
	df_binarizado=df_binarizado.rename(columns=lambda x: x.replace("-","_"))

	return df_binarizado

#Función que reporta las métricas para un modelo de regresión linear machine learning
from sklearn.metrics import mean_squared_error, r2_score
def report_scores(modelo_yhat, y_test):
	"""Reporta el error cuadrático promedio y r2_score. Se obtuvo del desafío
		'Regresión desde el aprendizaje de máquinas'
	Parametros:
		modelo_yhat(df.array): Vector calculado por el modelo
		y_test(df.array): Vector con datos reales que se comparará con modelo_yhat
	Retorno:
		Imprime el resultado de las métricas
	"""
	modelo_mse = mean_squared_error(y_test, modelo_yhat).round(2)
	modelo_r2 = r2_score(y_test, modelo_yhat).round(2)
	print(f"Error cuadrático promedio (mse): {modelo_mse}")
	print(f"R Cuadrado (R^2): {modelo_r2}")

#Función que lista las correlaciones entre un vector y las demas variables. Creamos la función en base a los ejemplos de la lectura respectiva
def fetch_features(df, vector_objetivo):
	"""Lista las correlaciones entre el vector objetivo y las demas variables. Se obtuvo del desafío
		'Regresión desde el aprendizaje de máquinas'
	Parametros:
		df(df): DataFrame
		vector_objetivo(str): Nombre del vector objetivo
	Retorno:
		Retorna un DataFrame con las correlaciones
	"""
	columnas = list(df.columns)
	attr_name, pearson_r, abs_pearson_r = [],[],[]
	for col in columnas:
		if col != vector_objetivo:
			attr_name.append(col)
			pearson_r.append(df[col].corr(df[vector_objetivo]))
			abs_pearson_r.append(abs(df[col].corr(df[vector_objetivo])))
	features = pd.DataFrame({
	  'attribute': attr_name,
		'corr':pearson_r,
		'abs_corr':abs_pearson_r
	})
	features = features.set_index('attribute')
	features = features.sort_values(by=['abs_corr'], ascending=False)
	return features

def errores(y_true, y_hat, modelo_nombre):
    print(f"Modelo {modelo_nombre} MAE -> {mean_absolute_error(y_true,y_hat)}")
    print(f"Modelo {modelo_nombre} MSE -> {mean_squared_error(y_true,y_hat)}")


def barras_por_atributo(df):
	n=1
	colores = ['tomato', 'lightblue', 'purple', 'yellow', 'green']
	#plt.figure(figsize=(15,15))
	for j in df.columns:
	    plt.subplot(int(len(list(df.columns))/3)+2,3,n)
	    ax=plt.bar(df[j].index, df[j], color=colores)
	    plt.title(j)
	    n+=1
	plt.tight_layout()


def muestra_boxplot(df, vector_objetivo):
    n=1
    plt.figure(figsize=(15,15))
    for j in df.drop(columns=vector_objetivo).columns:
        plt.subplot((len(list(df.columns))/3)+2,3,n)
        ax=sns.boxplot(x=j,data=df, orient='h')
        n+=1
    plt.tight_layout()
