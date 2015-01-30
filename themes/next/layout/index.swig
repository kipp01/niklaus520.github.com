{% extends '_layout.swig' %}
{% import '_macro/post.swig' as render %}

{% block title %} {{ config.title }} {% endblock %}

{% block content %}
  {% for post in page.posts %}
    {{ render.post(post) }}
  {% endfor %}

{% if (config.disqus_shortname) %}
  <div id="disqus_thread"></div>
  <script type="text/javascript">
  /* * * CONFIGURATION VARIABLES: EDIT BEFORE PASTING INTO YOUR WEBPAGE * * */
  var disqus_shortname = '{{config.disqus_shortname}}'; // required: replace example with your forum shortname
  /* * * DON'T EDIT BELOW THIS LINE * * */
  (function() {
      var dsq = document.createElement('script'); dsq.type = 'text/javascript'; dsq.async = true;
      dsq.src = '//' + disqus_shortname + '.disqus.com/count.js';
      (document.getElementsByTagName('head')[0] || document.getElementsByTagName('body')[0]).appendChild(dsq);
  })();
  </script>
  <noscript>Please enable JavaScript to view the <a href="https://disqus.com/?ref_noscript">comments powered by Disqus.</a></noscript>
  {% endif %}

{% endblock %}
