{% extends '_layout.swig' %}
{% import '_macro/post.swig' as render %}

{% block title %} {{ page.title }} | {{ config.title }} {% endblock %}

{% block page_class %}page-post-detail{% endblock %}

{% block content %}
  {{ render.post(page) }}

  {% if config.duoshuo and config.duoshuo.shortname and page.comments %}
    <div class="comments">
      <div class="ds-thread" data-thread-key="{{ page.path }}"
          data-title="{{ page.title }}" data-url="{{ page.permalink }}">
      </div>
    </div>
  {% endif %}

  {% if (post.comments && config.disqus_shortname) %}
    <div id="disqus_thread"></div>
    <a href="<%- post.permalink %>#disqus_thread" class="article-comment-link">Comments</a>
  {% endif %}

  {% if (config.disqus_shortname) %}
  <div class="comments">
  <div id="disqus_thread"></div>
  <script type="text/javascript">
  /* * * CONFIGURATION VARIABLES: EDIT BEFORE PASTING INTO YOUR WEBPAGE * * */
  var disqus_shortname = '{{config.disqus_shortname}}'; // required: replace example with your forum shortname
  /* * * DON'T EDIT BELOW THIS LINE * * */
  (function() {
      var dsq = document.createElement('script'); dsq.type = 'text/javascript'; dsq.async = true;
      dsq.src = '//' + disqus_shortname + '.disqus.com/{% if (page.comments) %}embed.js{%else %}count.js{% endif %}';
      (document.getElementsByTagName('head')[0] || document.getElementsByTagName('body')[0]).appendChild(dsq);
  })();
  </script>
  <noscript>Please enable JavaScript to view the <a href="https://disqus.com/?ref_noscript">comments powered by Disqus.</a></noscript>
  </div>
  {% endif %}

{% endblock %}
