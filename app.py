
import streamlit as st
from data import collect_resume_data
from resume_generator import ResumeGenerator

def main():
    st.set_page_config(page_title="Professional Resume Generator", layout="wide")
    
    st.title("Professional Resume Generator with AI Enhancement")
    st.markdown("""
    Create a professional resume with AI-enhanced content using Llama's language model. 
    Fill in your details below and let our system generate a polished resume.
    """)
    
    resume_data = collect_resume_data()
    
    if st.button("Generate Professional Resume"):
        if not resume_data["personal_info"]["name"]:
            st.error("Please enter at least your name to generate a resume.")
            return
            
        try:
            with st.spinner("Generating your professional resume with AI enhancement..."):
                generator = ResumeGenerator()
                pdf = generator.create_professional_pdf(resume_data)
                
                st.download_button(
                    label="Download Professional Resume (PDF)",
                    data=pdf,
                    file_name=f"{resume_data['personal_info']['name'].replace(' ', '_')}_professional_resume.pdf",
                    mime="application/pdf"
                )
                
                st.success("✨ Your professional resume has been generated successfully! Click above to download.")
            
        except Exception as e:
            st.error(f"Error generating PDF: {str(e)}")

if __name__ == "__main__":
    main()