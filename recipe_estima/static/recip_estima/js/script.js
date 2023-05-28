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

    function enableEditMode() {
        var field = document.getElementById("editable-field");
        var fieldValue = field.innerText;

        var inputField = document.createElement("input");
        inputField.type = "text";
        inputField.value = fieldValue;

        inputField.onblur = function() {
            var updatedValue = inputField.value;
            field.innerText = updatedValue;
            field.parentNode.removeChild(inputField);
        };

        field.innerText = "";
        field.appendChild(inputField);
        inputField.focus();
    }