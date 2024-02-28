import streamlit as st
import csv
import pandas

st.set_page_config(layout="wide")
st.markdown("<h1 style='text-align: center;'>Fizz - Assassin AP</h1>", unsafe_allow_html=True)
col1, col2 = st.columns(2)

with col1:
	st.image("images/fizz.jpg")
with col2:
	st.markdown("""Il y a longtemps, les océans de Runeterra abritaient des civilisations bien plus anciennes que celles des terres. Dans les profondeurs de ce que l'on appelle aujourd'hui la Mer du gardien se trouvait jadis une grande cité, et c'est là que Fizz, un yordle, avait élu domicile. Il vivait aux côtés des artisans et des guerriers de cette fière et noble race. Bien qu'il ne fût pas l'un d'entre eux, ils le traitaient en égal, car ils appréciaient toujours son esprit joueur et les récits de ses aventures rocambolesques.

Mais le monde changeait. Les océans se réchauffaient, poussant de redoutables prédateurs à quitter leurs fosses. Alors que d'autres colonies avaient cessé de donner signe de vie, les dirigeants de la grande cité n'étaient toujours pas d'accord sur la façon de répondre à cette menace. Fizz décida de ratisser les mers pour retrouver des survivants ou quiconque aurait des informations sur ce qu'il s'était passé.

Puis, en un jour funeste, arrivèrent les gigalodons.

Ces gigantesques requins-dragons immobilisaient leur proie d'un simple cri, et les avenues de la grande cité furent vite baignées de rouge. Des milliers périrent en quelques heures ; dans leur fureur, les monstres marins fracassèrent les tours et les temples. L'odeur du sang dans l'eau parvint jusqu'à Fizz, et celui-ci rebroussa chemin à toute vitesse, déterminé à participer au combat et à sauver la cité.

Malheureusement, il arriva trop tard. Il ne restait plus rien de la cité. Lorsque les débris de la destruction retombèrent, il n'y avait pas le moindre survivant, tous les bâtiments étaient en ruines et les gigalodons étaient partis. Seul dans les profondeurs glacées, Fizz se laissa submerger par un immense désespoir. Alors que sa magie yordle commençait à se dissiper, il se laissa emporter par le courant, dérivant dans un état catatonique, perdu dans ses rêves pendant des millénaires…
	""")

col3, col4 = st.columns(2)
data = pandas.read_csv("data.csv", delimiter=",")
middle = int(len(data) / 2)

with col3:
	for index, elem in data[:middle].iterrows():
		st.title(elem["name"])
		st.image("images/" + elem["image"])
		st.markdown(elem["description"])

with col4:
	for index, elem in data[middle:].iterrows():
		st.title(elem["name"])
		st.image("images/" + elem["image"])
		st.markdown(elem["description"])

