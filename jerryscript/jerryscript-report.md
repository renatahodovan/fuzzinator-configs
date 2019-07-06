###### JerryScript revision
{{version}}

###### Build platform
{{platform}}

###### Build steps
```
{{build_command}}
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
```
{{stderr}}
```
{% endif %}

{% if backtrace %}
###### Backtrace
```
{{backtrace}}
```
{% endif %}

<sup>Found by [Fuzzinator](http://fuzzinator.readthedocs.io/) with {{fuzzer}}. </sup>
