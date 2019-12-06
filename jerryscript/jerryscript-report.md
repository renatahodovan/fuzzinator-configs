###### JerryScript revision
{{version}}

###### Build platform
{{platform}}

###### Build steps
```
{{build_command|replace('\n', ' \\\n'}}
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
{{stderr}}
```
{% endif %}

{% if backtrace %}
###### Backtrace
```text
{{backtrace}}
```
{% endif %}

<sup>Found by [Fuzzinator](http://fuzzinator.readthedocs.io/) with {{fuzzer}}. </sup>
