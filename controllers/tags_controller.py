from flask import Blueprint, Flask, redirect, render_template, request

from models.tag import Tag
import repositories.tag_repository as tag_repository

tags_blueprint = Blueprint("tags", __name__)

# Categories index
@tags_blueprint.route("/categories")
def tags():
    tags = tag_repository.select_all()
    return render_template("/categories/index.html", tags=tags)

# Add tag
@tags_blueprint.route("/categories/add")
def add_tag():
    return render_template("/categories/add.html")

# Create categories and return to category landing page
@tags_blueprint.route("/categories", methods=["POST"])
def create_tag():
    category = request.form["category"]
    new_tag = Tag(category)
    tag_repository.save(new_tag)
    return redirect("/categories")

# Edit category
@tags_blueprint.route("/categories/<id>/edit")
def edit_tag(id):
    tag = tag_repository.select(id)
    return render_template("/categories/edit.html", tag=tag)
       
# Update category and return to category landing page
@tags_blueprint.route("/categories/<id>", methods=["POST"])
def update_tag(id):
    category = request.form["category"]
    tag = Tag(category, id)
    tag_repository.update(tag)
    return redirect("/categories") 
    
