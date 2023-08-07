<!doctype html>
<title>{% block title %}{% endblock %} - Flaskr</title>
<link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
<nav>
  <h1><a href="{{ url_for('blog.index') }}">Flaskr</a></h1>
  <ul>
    {% if current_user.is_authenticated %}
      <li><a href="{{ url_for('admin.admin_panel') }}">Dashboard</a></li>
      <li><a href="{{ url_for('admin.create_role') }}">Create roles</a></li>
      <li><a href="{{ url_for('admin.bind_roles_with_user') }}">Bind roles with users</a></li>
      <li><span>{{ current_user.username }}</span>
      <li><a href="{{ url_for('auth.logout') }}">Log Out</a>
    {% else %}
      <li><a href="{{ url_for('auth.register') }}">Register</a>
      <li><a href="{{ url_for('auth.login') }}">Log In</a>
    {% endif %}
  </ul>
</nav>
<section class="content">
  <header>
    {% block header %}{% endblock %}
  </header>
  {% for message in get_flashed_messages() %}
    <div class="flash">{{ message }}</div>
  {% endfor %}
  {% block content %}{% endblock %}
</section>

{% block scripts %}{% endblock %}