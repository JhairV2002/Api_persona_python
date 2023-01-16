from rest_framework import serializers
from personas_fk_api.models import Persona, Genero, TipoEstudiante
from personas_fk_api.deserializer import attempt_json_deserialize


class TipoEstudianteSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoEstudiante
        fields = ["id", "descripcion"]


class GeneroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genero
        fields = ["id", "descripcion"]


class PersonaSerializer(serializers.ModelSerializer):
    tipoEstudiante = TipoEstudianteSerializer(read_only=True)
    genero = GeneroSerializer(read_only=True)

    def create(self, validated_data):
        request = self.context["request"]

        tipoEstudiante_data = request.data.get("tipoEstudiante")
        tipoEstudiante_data = attempt_json_deserialize(
            tipoEstudiante_data, expect_type=dict
        )
        tipoEstudiante = TipoEstudiante.objects.get(
            descripcion=tipoEstudiante_data["descripcion"]
        )
        validated_data["tipoEstudiante"] = tipoEstudiante

        genero_data = request.data.get("genero")
        genero_data = attempt_json_deserialize(genero_data, expect_type=dict)
        genero = Genero.objects.get(descripcion=genero_data["descripcion"])
        validated_data["genero"] = genero

        instance = super().create(validated_data)

        return instance

    def update(self, instance, validated_data):
        request = self.context["request"]

        tipoEstudiante_data = request.data.get("tipoEstudiante")
        tipoEstudiante_data = attempt_json_deserialize(
            tipoEstudiante_data, expect_type=dict
        )
        tipoEstudiante = TipoEstudiante.objects.get(
            descripcion=tipoEstudiante_data["descripcion"]
        )
        validated_data["tipoEstudiante"] = tipoEstudiante

        genero_data = request.data.get("genero")
        genero_data = attempt_json_deserialize(genero_data, expect_type=dict)
        genero = Genero.objects.get(descripcion=genero_data["descripcion"])
        validated_data["genero"] = genero

        instance = super().update(instance, validated_data)

        return instance

    class Meta:
        model = Persona
        fields = [
            "id",
            "identificacion",
            "nombre",
            "apellido",
            "edad",
            "tipoEstudiante",
            "genero",
        ]
