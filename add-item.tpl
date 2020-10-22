<html>
<head>
</head>

<body>
    <h4>Add new item</h4>
    <form action="/todo-list/add-item" method="POST">
        <input type="text" name="item_name" placeholder="Item name"/>
        <input type="submit" name="add" value="Add"/>
    </form>
    <br>
    <a href="/todo-list">Go back</a>
</body>
</html>