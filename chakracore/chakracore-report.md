###### ChakraCore version:

```
Checked revision: {{version}}
Build command: {{build_command}}
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
{{stderr}}
{{backtrace}}
```

<sup>Found by [Fuzzinator](http://fuzzinator.readthedocs.io/) with {{fuzzer}}. </sup>
