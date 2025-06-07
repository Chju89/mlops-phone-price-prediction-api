{{- define "fastapi.name" -}}
{{- default .Chart.Name .Values.nameOverride | trunc 63 | trimSuffix "-" -}}
{{- end -}}

{{- define "fastapi.fullname" -}}
{{- printf "%s-%s" .Release.Name (include "fastapi.name" .) | trunc 63 | trimSuffix "-" -}}
{{- end -}}

