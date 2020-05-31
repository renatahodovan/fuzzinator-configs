###### JerryScript revision
{{version|trim}}

###### Build platform
{{platform}}

###### Build steps
```
{{build_command|replace('\n', ' \\\n')|trim}}
```

###### Test case
```javascript
{% if reduced %}
{{reduced}}
{% else %}
{{test}}
{% endif %}
```

{% if stderr %}
###### Output
```text
{{stderr|trim}}
```
{% endif %}

{% if backtrace %}
###### Backtrace
```text
{{backtrace|trim}}
```
{% endif %}

<sup>Found by [Fuzzinator](http://fuzzinator.readthedocs.io/) with {{fuzzer}}. </sup>
