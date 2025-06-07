{{- define "mlflow.name" -}}
mlflow
{{- end -}}

{{- define "mlflow.fullname" -}}
{{ .Release.Name }}-mlflow
{{- end -}}

