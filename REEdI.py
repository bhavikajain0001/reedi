import streamlit as st
import streamlit.components.v1 as components
from PIL import Image

st.set_page_config(page_title="REEdI Career Pathway Planning Platform", page_icon="💡", layout="wide")
overall_streamlit_style = """
			<style>		
			@import url('https://fonts.googleapis.com/css2?family=Roboto:wght@100&display=swap');

			#MainMenu {
			visibility: hidden;
			}

			footer {
				visibility: hidden;
			}

			.css-hxt7ib {
      			margin-top: -75px;
    		}

			.appview-container .main .block-container {
                    padding-top: 3rem; 
                    padding-right:1rem;
                    padding-left: 1rem;
                    padding-bottom:0.5rem;
            }
		
			html, body, [class*="css"] {
			font-family: 'Roboto', 'sans-serif';
			}		

			.sidebar .sidebar-content {
				background-color: #000000 !important;
				text-color: #00a79e
			}

			.sidebar-text {
   				font-size:20px !important;
			}
			</style>
			"""

st.markdown(overall_streamlit_style, unsafe_allow_html=True)
		
# structuring the side bar menu
def sidebar_info():
	st.sidebar.markdown(overall_streamlit_style, unsafe_allow_html=True)
	st.sidebar.title('💡 REEdI Career Pathway Planning Project')
	st.sidebar.markdown("""
                   The Career Pathway Planning Project aims to align the REEdI program with industry needs to produce successful graduates and provide them with career planning support. It incorporates two major elements:""")
	st.sidebar.markdown("""1. REEdI Course Modules Skillification to measure skills in supply""") 
	st.sidebar.markdown("""2. Job postings data analysis to measure the skills in demand""") 

def main():
	image_1 = Image.open('/app/images/logo_1.png')
	page = st.sidebar.selectbox("Choose the Platform", ["REEdI Modules' Skillification Platform", "Skills-In-Demand Analysis"])
	if page == "REEdI Modules' Skillification Platform":
		col1, mid, col2 = st.columns([8,1,37])
		with col1:
			st.image(image_1, use_column_width=True)
		with col2:
			st.markdown('<p style="font-family:Roboto;font-size:60px;font-weight:bold"> 🎓 REEdI Modules Skillification Platform </p>', unsafe_allow_html=True)
		html_temp = """
			<div class='tableauPlaceholder' id='viz1683884933680' style='position: relative'>
				<noscript>
					<a href='#'><img alt='REEdI Modules&#39; Skillification ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;RE&#47;REEdICoursesSkillification&#47;REEdICoursesSkillification&#47;1_rss.png' style='border: none' /></a>
				</noscript>
				<object class='tableauViz' style='display:none;'>
					<param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' />
					<param name='embed_code_version' value='3' />
					<param name='site_root' value='' />
					<param name='name' value='REEdICoursesSkillification&#47;REEdICoursesSkillification' />
					<param name='tabs' value='no' />
					<param name='toolbar' value='yes' />
					<param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;RE&#47;REEdICoursesSkillification&#47;REEdICoursesSkillification&#47;1.png' />
					<param name='animate_transition' value='yes' />
					<param name='display_static_image' value='yes' />
					<param name='display_spinner' value='yes' />
					<param name='display_overlay' value='yes' />
					<param name='display_count' value='yes' />
					<param name='language' value='en-GB' />
				</object>
			</div>
			<script type='text/javascript'>
			var divElement = document.getElementById('viz1683884933680');
			var vizElement = divElement.getElementsByTagName('object')[0];
			vizElement.style.width = '100%';
			vizElement.style.height = (divElement.offsetWidth * 0.75) + 'px';
			var scriptElement = document.createElement('script');
			scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';
			vizElement.parentNode.insertBefore(scriptElement, vizElement);
			</script>
			"""
		components.html(html_temp, width=1400, height=1000)

	elif page == "Skills-In-Demand Analysis":
		col1, mid, col2 = st.columns([8,1,37])
		with col1:
			st.image(image_1, use_column_width=True)
		with col2:
			st.markdown('<p style="font-family:Roboto;font-size:60px;font-weight:bold">🎓 Skills-In-Demand Analysis </p>', unsafe_allow_html=True)
		html_temp = """
			<div class='tableauPlaceholder' id='viz1684495388691' style='position: relative'>
			<noscript>
				<a href='#'><img alt='Demand - MTU ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;De&#47;Demand-MTU&#47;Demand-MTU&#47;1_rss.png' style='border: none' /></a>
			</noscript>
			<object class='tableauViz' style='display:none;'>
				<param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' />
				<param name='embed_code_version' value='3' />
				<param name='site_root' value='' />
				<param name='name' value='Demand-MTU&#47;Demand-MTU' />
				<param name='tabs' value='no' />
				<param name='toolbar' value='yes' />
				<param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;De&#47;Demand-MTU&#47;Demand-MTU&#47;1.png' />
				<param name='animate_transition' value='yes' />
				<param name='display_static_image' value='yes' />
				<param name='display_spinner' value='yes' />
				<param name='display_overlay' value='yes' />
				<param name='display_count' value='yes' />
				<param name='language' value='en-GB' />
			</object>
			</div>
			<script type='text/javascript'>
				var divElement = document.getElementById('viz1684495388691');
				var vizElement = divElement.getElementsByTagName('object')[0];
				if(divElement.offsetWidth > 800) {
					vizElement.style.width = '1204px';
					vizElement.style.height = '1835px';
				} else if(divElement.offsetWidth > 500) {
					vizElement.style.width = '1204px';
					vizElement.style.height = '1835px';
				} else {
					vizElement.style.width = '100%';
					vizElement.style.height = '1827px';
				}
				var scriptElement = document.createElement('script');
				scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';
				vizElement.parentNode.insertBefore(scriptElement, vizElement);
			</script>
			"""
		components.html(html_temp, width=1500, height=1800)

def footer():
    st.markdown('<div style=font-size:15px>Powered by Abodoo</div>', unsafe_allow_html=True)
    
# the controller
def load_page():
    sidebar_info()
    main()
    footer()

if __name__ == "__main__":    
	load_page()
