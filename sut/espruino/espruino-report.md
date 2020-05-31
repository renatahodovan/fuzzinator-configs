###### Espruino version:

```
Checked revision: {{version|trim}}
Build command: {{build_command|trim}}
```

###### OS:

```
{{platform}}
```

###### Test case:

```javascript
{% if reduced %}
{{reduced}}
{% else %}
{{test}}
{% endif %}
```

###### Backtrace:

```text
{{stderr|trim}}
{{backtrace|trim}}
```

<sup>Found by [Fuzzinator](http://fuzzinator.readthedocs.io/) with {{fuzzer}}. </sup>
