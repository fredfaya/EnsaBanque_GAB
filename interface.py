import streamlit as st
import pandas as pd
import numpy as np
import streamlit.components.v1 as components
from PIL import Image

# les variables pour controller l'affichage
transfert_found = False
transfert_received = {

}
agentId = 0
firstName = "Agent"
lastName = "Agent"
date = "23/23/2023"
amount = 10000
receiverFirstName = "FAYA"
receiverLastName = "Frederic"


img = Image.open("./images/money.jpg")
st.image(img, width=100)

components.html(
    """
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
    <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
    <div style="background-color: red">
        <div class="h2 p-3 border" style="background-color: #3286E6;color : #fff ;text-align: center;">
            ENSA GAB
        </div>
    </div>

    """,
    height=100,

)
columns = st.columns((1.75, 2, 1))
columns[1].markdown("# :red[GAB Menu]")
components.html(
    """
        <div style = "height:100px;">
        </div>
        """,
    height=20,
)
columns_choice = st.columns((0.75, 2))
choice = columns_choice[1].radio("Please select a service", ('Service 1', 'Service 2', 'Other Service'), horizontal=True)
components.html(
    """
        <div style = "height:100px;">
        </div>
        """,
    height=20,
)
if choice == 'Other Service' and not transfert_found:

    ref = st.text_input("Enter the transfert reference", placeholder="Enter your transfert reference")
    pin = st.text_input("Enter the PIN code", placeholder="Enter your PIN code")

    components.html(
        """
        <div style = "height:100px;">
        </div>
        """,
        height=20,
    )

    columns_button_search = st.columns((2.25, 1, 2))
    if columns_button_search[1].button('Search'):
        components.html(
            """
            <div style = "height:100px;">
            </div>
            """,
            height=20,
        )
        transfert_reference = ref.title()
        transfert_pin = pin.title()

        transfert_found = True
        columns_infos_title = st.columns((0.65, 2, 0.15))
        columns_infos = st.columns((0.30, 2, 0.25))
        if transfert_found:
            columns_infos_title[1].header("TRANSFERT INFORMATIONS")
            st.markdown(
                """
                <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
                <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.6.1/dist/css/bootstrap.min.css" integrity="sha384-zCbKRCUGaJDkqS1kPbPd7TveP5iyJE0EjAuZQTgFLD2ylzuqKfdKlfG/eSrtxUkn" crossorigin="anonymous">
                
                <div class="shadow bg-primary rounded pt-5 pb-5">
                    <div class="row m-auto d-flex justify-content-between p-3 bg-white w-75 rounded-top">
                        <div class="form-label" style="font-weight: bold;">Agent ID</div>
                        <div style="color: #3286E6; font-size: 20px; padding-left:50px"> {} </div>
                    </div>
                    <div class="row m-auto d-flex justify-content-between p-3 bg-white w-75">
                        <div class="form-label" style="font-weight: bold;">First Name</div>
                        <div style="color: #3286E6; font-size: 20px; padding-left:50px"> {} </div>
                    </div>
                    <div class="row m-auto d-flex justify-content-between p-3 bg-white w-75">
                        <div class="form-label" style="font-weight: bold;">Last Name</div>
                        <div style="color: #3286E6; font-size: 20px; padding-left:50px"> {} </div>
                    </div>
                    <div class="row m-auto d-flex justify-content-between p-3 bg-white w-75">
                        <div class="form-label" style="font-weight: bold;">Date of issue</div>
                        <div style="color: #3286E6; font-size: 20px; padding-left:50px"> {} </div>
                    </div>
                    <div class="row m-auto d-flex justify-content-between p-3 bg-white w-75">
                        <div class="form-label" style="font-weight: bold;">Amount</div>
                        <div style="color: #3286E6; font-size: 20px; padding-left:50px"> {} </div>
                    </div>
                    <div class="row m-auto d-flex justify-content-between p-3 bg-white w-75">
                        <div class="form-label" style="font-weight: bold;">Receiver First Name</div>
                        <div style="color: #3286E6; font-size: 20px; padding-left:50px"> {} </div>
                    </div>
                    <div class="row m-auto d-flex justify-content-between p-3 bg-white w-75 rounded-bottom">
                        <div class="form-label" style="font-weight: bold;">Receiver Last Name</div>
                        <div style="color: #3286E6; font-size: 20px; padding-left:50px"> {} </div>
                    </div>
                </div>    

                """.format(agentId, firstName, lastName, date, amount, receiverFirstName, receiverLastName)
                ,
                unsafe_allow_html=True
            )
            components.html(
                """
                <div style = "height:100px;">
                </div>
                """,
                height=20,
            )
            columns_button_validate = st.columns((2.2, 1, 2))
            if columns_button_validate[1].button('Validate Payment', type='primary'):
                st.success("Transfert Validated!")
        else:
            columns_infos[1].error("Not transfert found !")


else:
    st.warning("You have to choose other service to get your transfert")

