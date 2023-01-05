from rest_framework import serializers

from .models import Schedule


class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = ["id", "date", "hour", "is_done", "user_id"]

    def create(self, validated_data):
        return Schedule.objects.create(**validated_data)


#  def create(self, validated_data: dict):
#         traits_list = validated_data.pop("traits")
#         group_obj = validated_data.pop("group")

#         group = Group.objects.create(**group_obj)
#         pet = Pet.objects.create(group=group, **validated_data)

#         for trait_dict in traits_list:
#             trait_obj, created = Trait.objects.get_or_create(
#                 **trait_dict,
#             )
#             pet.traits.add(trait_obj)
#         return pet
