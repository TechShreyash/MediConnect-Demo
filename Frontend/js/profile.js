document.getElementById('roleForm').addEventListener('submit', function (event) {
    event.preventDefault();
    const role = document.getElementById('role').value;
    if (role) {
        if (role === 'user') {
            window.location.href = 'user.html';

        }
        else {
            window.location.href = 'Ent_store.html';
        }
    } else {
        alert('Please select a role before continuing.');
    }
});
