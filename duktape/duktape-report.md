###### Duktape version:

```
Checked revision: {{version}}
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

```
{{stderr}}
{{backtrace}}
```

###### Build script:

```bash
{{build_command}}
```

###### fuzz.yaml:

```yaml
{{build_config}}
```

<sup>Found by [Fuzzinator](http://fuzzinator.readthedocs.io/) with {{fuzzer}}. </sup>
