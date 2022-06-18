import streamlit as st
import streamlit.components.v1 as components

def show_cards(company, file_count, recent_file):
    return components.html(
    f"""
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
    <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
    <div class="row">
        <div class="col-sm">
            <div class="card">
            <div class="card-body">
            <h6 class="card-title">No. of {company}'s Processed Files</h6>
            <h6 class="card-subtitle">{file_count}</h6>
            </div>
            </div>
        </div>
        <div class="col-sm">
            <div class="card">
            <div class="card-body">
            <h6 class="card-title">{company}'s Latest File</h6>
            <h6 class="card-subtitle">{recent_file}</h6>
            </div>
            </div>
        </div>
    
    </div>
    
    """,
)
