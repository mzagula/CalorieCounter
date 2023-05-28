function showRecipe(recipeId) {
    window.location.href = `/recip_estima/recipe_detail/${recipeId}`;
}
function showConfirmationDialog(recipeId) {
    document.getElementById("confirmation-dialog").style.display = "block";
}
function hideConfirmationDialog() {
    document.getElementById("confirmation-dialog").style.display = "none";
}
function deleteRecipe(recipeId) {
    window.location.href = `/recip_estima/recipe_delete/${recipeId}`;
}

var inputField = null;
function enableEditMode() {
    var editableField = document.getElementById("editable-field");
    var fieldValue = editableField.innerText;

    if (inputField === null) {
        inputField = document.createElement("input");
        inputField.type = "text";
        inputField.value = fieldValue;

        inputField.onblur = function () {
            saveChanges();
        };

        inputField.addEventListener("keypress", function(event) {
            if (event.key === "Enter") {
                saveChanges();
             }
         });
        editableField.innerText = "";
        editableField.appendChild(inputField);
        inputField.focus();
    };
}

function saveChanges() {
    var editableField = document.getElementById("editable-field");
    var updatedValue = inputField.value;
    editableField.innerText = updatedValue;
    inputField.parentNode.removeChild(inputField);
    inputField = null;
}
