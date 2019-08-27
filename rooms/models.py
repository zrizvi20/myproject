from django.db import models

# Create your models here.

class ProjectRoomTypes(models.Model):
    room_type_id = models.AutoField(primary_key=True)
    BEDROOM = 'bedroom'
    BATHROOM = 'bathroom'
    KITCHEN = 'kitchen'
    DRESSING_ROOM = 'dressing room'
    room_type_names = (
        (BEDROOM, 'bedroom'),
        (BATHROOM, 'bathroom'),
        (KITCHEN, 'kitchen'),
        (DRESSING_ROOM, 'dressing room')
        )
    room_type_name = models.CharField (
        max_length=150,
        choices=room_type_names,
        default=BEDROOM,
        verbose_name = 'Room Type'
        )
    room_type_desc = models.CharField(max_length=150, blank=True, verbose_name = 'Room Type Description')
    room_type_desc_1 = models.CharField(max_length=150, blank=True, verbose_name = 'Room Type Description')
    project_type = models.ForeignKey('projects.ProjectTypes', on_delete=models.CASCADE, verbose_name = 'Project Type')

    def __str__(self):
        return self.room_type_name

    class Meta:
        verbose_name = 'Project Room Types'
        verbose_name_plural = 'Project Room Types'


class FloorRooms(models.Model):
    room_id = models.AutoField(primary_key=True)
    BEDROOM = 'bedroom'
    BATHROOM = 'bathroom'
    KITCHEN = 'kitchen'
    DRESS_ROOM = 'dressing room'
    floor_room_types = (
        (BEDROOM, 'bed'),
        (BATHROOM, 'bathroom'),
        (KITCHEN, 'kitchen'),
        (DRESS_ROOM, 'dressing room'),
        )
    floor_room_name = models.CharField(
        max_length=150,
        choices=floor_room_types,
        default=BEDROOM,
        verbose_name = 'Room Type'
        )
    room_desc = models.CharField(max_length=150, blank=True, verbose_name = 'Room Description')
    room_desc_2 = models.CharField(max_length=150, blank=True, verbose_name = 'Room Description')
    room_covered_area = models.DecimalField(max_digits=5, decimal_places=2, verbose_name = 'Room Covered Area')
    covered_area_units = models.ForeignKey('units.CoveredAreaUnits', on_delete=models.CASCADE, verbose_name = 'Covered Area Unit')
    room_type = models.ForeignKey('rooms.ProjectRoomTypes', on_delete=models.CASCADE, verbose_name = 'Room Type')
    floor = models.ForeignKey('floors.ProjectFloors', on_delete=models.CASCADE, verbose_name = 'Floor')

    def __str__(self):
        return self.floor_room_name

    class Meta:
        verbose_name = 'Floor Rooms'
        verbose_name_plural = 'Floor Rooms'
    
class RoomSides(models.Model):
    room_side_id = models.AutoField(primary_key=True)
    FLOOR = 'floor'
    ROOF = 'roof'
    WALL_1 = 'wall 1'
    WALL_2 = 'wall 2'
    WALL_3 = 'wall 3'
    WALL_4 = 'wall 4'
    room_side_names = (
        (FLOOR, 'floor'),
        (ROOF, 'roof'),
        (WALL_1, 'wall 1'),
        (WALL_2, 'wall 2'),
        (WALL_3, 'wall 3'),
        (WALL_4, 'wall 4'),
        )
    room_side_name = models.CharField(
        max_length=150,
        choices=room_side_names,
        default=FLOOR,
        verbose_name = 'Room Side'
        )
    room_side_desc_1 = models.CharField(max_length=150, blank=True, verbose_name = 'Room Side Description')
    room_side_desc_2 = models.CharField(max_length=150, blank=True, verbose_name = 'Room Side Description')
    room_side_covered_area = models.DecimalField(max_digits=5, decimal_places=2, verbose_name = 'Room Side Covered Area')
    room_side_length = models.DecimalField(max_digits=5, decimal_places=2, verbose_name = 'Room Side Length')
    room_side_width = models.DecimalField(max_digits=5, decimal_places=2, verbose_name = 'Room Side Width')
    length_unit = models.ForeignKey('units.LengthUnits', on_delete=models.CASCADE, verbose_name = 'Length Unit')
    room = models.ForeignKey(FloorRooms, on_delete=models.CASCADE, verbose_name = 'Room')

    def __str__(self):
        return self.room_side_name

    class Meta:
        verbose_name = 'Room Sides'
        verbose_name_plural = 'Room Sides'

