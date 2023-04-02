function changeCheckboxValue(checkbox) {
    if (checkbox.checked) {
        checkbox.value = 'checked';
    } else {
        checkbox.value = 'unchecked';
    }
}