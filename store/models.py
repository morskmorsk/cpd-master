from django.db import models
from users.models import CustomUser
from datetime import datetime, timezone
from django.core.validators import MinValueValidator
# from phonenumber_field.modelfields import PhoneNumberField
# import phonenumbers
# /////////////////////////////////////////////////////////////////////////////////
STATE_CHOICES = (
    ('AL', 'Alabama'),
    ('AK', 'Alaska'),
    ('AZ', 'Arizona'),
    ('AR', 'Arkansas'),
    ('CA', 'California'),
    ('CO', 'Colorado'),
    ('CT', 'Connecticut'),
    ('DE', 'Delaware'),
    ('DC', 'District Of Columbia'),
    ('FL', 'Florida'),
    ('GA', 'Georgia'),
    ('HI', 'Hawaii'),
    ('ID', 'Idaho'),
    ('IL', 'Illinois'),
    ('IN', 'Indiana'),
    ('IA', 'Iowa'),
    ('KS', 'Kansas'),
    ('KY', 'Kentucky'),
    ('LA', 'Louisiana'),
    ('ME', 'Maine'),
    ('MD', 'Maryland'),
    ('MA', 'Massachusetts'),
    ('MI', 'Michigan'),
    ('MN', 'Minnesota'),
    ('MS', 'Mississippi'),
    ('MO', 'Missouri'),
    ('MT', 'Montana'),
    ('NE', 'Nebraska'),
    ('NV', 'Nevada'),
    ('NH', 'New Hampshire'),
    ('NJ', 'New Jersey'),
    ('NM', 'New Mexico'),
    ('NY', 'New York'),
    ('NC', 'North Carolina'),
    ('ND', 'North Dakota'),
    ('OH', 'Ohio'),
    ('OK', 'Oklahoma'),
    ('OR', 'Oregon'),
    ('PA', 'Pennsylvania'),
    ('RI', 'Rhode Island'),
    ('SC', 'South Carolina'),
    ('SD', 'South Dakota'),
    ('TN', 'Tennessee'),
    ('TX', 'Texas'),
    ('UT', 'Utah'),
    ('VT', 'Vermont'),
    ('VA', 'Virginia'),
    ('WA', 'Washington'),
    ('WV', 'West Virginia'),
    ('WI', 'Wisconsin'),
    ('WY', 'Wyoming'),
)
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////
SERVICE_PROVIDER_CHOICES = (
    ('N/A', 'n/a'),
    ('At&t', 'at&t'),
    ('T-mobile', 't-mobile'),
    ('Verizon', 'verizon'),
    ('Metro', 'metro'),
    ('Cricket', 'cricket'),
    ('Simple Mobile', 'simple mobile'),
    ('H20', 'h20'),
    ('Lyca Mobile', 'lyca mobile'),
    ('Ultra Mobile', 'ultra mobile'),
    ('Net 10', 'net 10'),
    ('Straight Talk', 'straight talk'),
    ('Tracfone', 'tracfone'),
    ('Boost Mobile', 'boost mobile'),
    ('Virgin Mobile', 'virgin mobile'),
    ('Sprint', 'sprint'),
    ('Unlocked', 'unlocked'),
    ('Other', 'other'),
    ('Unknown', 'unknown'),
    ('آخر', 'آخر'),
)
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////
COMPATIBILITY_CHOICES = (
    ('GSM', 'gsm'),
    ('CDMA', 'cdma'),
    ('GSM/CDMA', 'gsm/cdma'),
    ('Other', 'other'),
    ('Unknown', 'unknown'),
    ('آخر', 'آخر'),
    ('N/A', 'n/a'),
)
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////
WORK_ORDER_STATUS_CHOICES = (
    ('Pending', 'pending'),
    ('In Progress', 'in progress'),
    ('Completed', 'completed'),
    ('Back Ordered', 'back ordered'),
    ('Beyond Repair', 'beyond repair'),
    ('Cannot be Repaired', 'cannot be repaired'),
    ('Cancelled', 'cancelled'),
    ('Rejected', 'rejected'),
    ('Unknown', 'unknown'),
    ('آخر', 'آخر'),
)
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////
DEVICE_CONDITION_CHOICES = (
    ('New', 'new'),
    ('Used', 'used'),
    ('Refurbished', 'refurbished'),
    ('Repaired', 'repaired'),
    ('Available', 'available'),
    ('Unavailable', 'unavailable'),
    ('Reserved', 'reserved'),
    ('Recycled', 'recycled'),
    ('Unknown', 'unknown'),
    ('آخر', 'آخر'),
)
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////
DEVICE_GRADE_CHOICES = (
    ('A', 'a'),
    ('B', 'b'),
    ('C', 'c'),
    ('D', 'd'),
    ('Unknown', 'unknown'),
)
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////
DEVICE_TYPE_CHOICES = (
    ('Smartphone', 'smartphone'),
    ('Tablet', 'tablet'),
    ('Laptop', 'laptop'),
    ('Desktop', 'desktop'),
    ('Other', 'other'),
    ('Unknown', 'unknown'),
    ('آخر', 'آخر'),
)
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////
DEVICE_BRAND_CHOICES = (
    ('Apple', 'apple'),
    ('Samsung', 'samsung'),
    ('LG', 'lg'),
    ('HTC', 'htc'),
    ('Motorola', 'motorola'),
    ('Nokia', 'nokia'),
    ('Huawei', 'huawei'),
    ('ZTE', 'zte'),
    ('Alcatel', 'alcatel'),
    ('Blackberry', 'blackberry'),
    ('Sony', 'sony'),
    ('Microsoft', 'microsoft'),
    ('Asus', 'asus'),
    ('Lenovo', 'lenovo'),
    ('Acer', 'acer'),
    ('Toshiba', 'toshiba'),
    ('Dell', 'dell'),
    ('HP', 'hp'),
    ('Other', 'other'),
    ('Unknown', 'unknown'),
    ('آخر', 'آخر'),
)
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////
LABOR_RISK_CHOICES = (
    ('Minimal', 'minimal'),
    ('very low', 'very low'),
    ('Low', 'low'),
    ('Medium', 'medium'),
    ('High', 'high'),
    ('Very High', 'very high'),
    ('Too High', 'too high'),
)
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////


class Manufacturer(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

    def __repr__(self) -> str:
        return self.name

    class Meta:
        ordering = ('id',)
        verbose_name = 'Manufacturer'
        verbose_name_plural = 'Manufacturers'
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////


class Brand(models.Model):
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.manufacturer.name + " " + self.name

    def __repr__(self) -> str:
        return self.manufacturer.name + " " + self.name

    class Meta:
        ordering = ('id',)
        verbose_name = 'Device Brand'
        verbose_name_plural = 'Device Brands'
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////


class DeviceModel(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    model_series = models.CharField(max_length=50, default="N/A")
    name = models.CharField(max_length=50)

    def __str__(self):
        return (self.brand.manufacturer.name
                + " "
                + self.brand.name
                + " "
                + self.name
                )

    def __repr__(self) -> str:
        return (self.brand.manufacturer.name
                + " "
                + self.brand.name
                + " "
                + self.name
                )

    class Meta:
        ordering = ('id',)
        verbose_name = 'Device Model'
        verbose_name_plural = 'Device Models'
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////


class DeviceColor(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

    def __repr__(self) -> str:
        return self.name

    class Meta:
        ordering = ('id',)
        verbose_name = 'Device Color'
        verbose_name_plural = 'Device Colors'
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////


class Vendor(models.Model):
    name = models.CharField(max_length=200)
    contact_name = models.CharField(max_length=200, default="Unknown")
    phone = models.CharField(max_length=200, default="Unknown")
    email = models.CharField(max_length=200, default="Unknown")
    address = models.CharField(max_length=200, default="Unknown")

    def __str__(self):
        return self.name

    def __repr__(self):
        return '<Vendor object ({})>'.format(self.id)

    class Meta:
        ordering = ('id',)
        verbose_name = 'Vendor'
        verbose_name_plural = 'Vendors'
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////


class DeviceDefect(models.Model):
    defect_name = models.CharField(max_length=50, unique=True)
    defect_description = models.TextField(
        max_length=500, blank=True, null=True)
    defect_solution = models.TextField(max_length=500, default="Unknown")

    def __str__(self):
        return self.defect_name

    def __repr__(self) -> str:
        return self.defect_name

    class Meta:
        ordering = ('id',)
        verbose_name = 'Device Defect'
        verbose_name_plural = 'Device Defects'
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////


class Department(models.Model):
    name = models.CharField(max_length=200)
    taxable_choices = (
        ('Yes', 'yes'),
        ('No', 'no'),
    )
    taxable = models.CharField(
        max_length=3, choices=taxable_choices, default='yes')

    def __str__(self):
        return self.name

    def __repr__(self):
        return '<Department object ({})>'.format(self.id)

    class Meta:
        ordering = ('id',)
        verbose_name = 'Department'
        verbose_name_plural = 'Departments'
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////


class Location(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=500, blank=True, null=True)
    address = models.CharField(max_length=200, default="Unknown")

    def __str__(self):
        return self.name

    def __repr__(self):
        return '<Location object ({})>'.format(self.id)

    class Meta:
        ordering = ('id',)
        verbose_name = 'Location'
        verbose_name_plural = 'Locations'
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////


class Device(models.Model):
    owner = models.ForeignKey(CustomUser,
                              on_delete=models.CASCADE,
                              related_name='device_owner',
                              blank=True,
                              null=True
                              )
    department = models.ForeignKey(
        Department, on_delete=models.CASCADE, related_name='device_department')
    location = models.ForeignKey(Location, on_delete=models.CASCADE, default=1)
    device_model = models.ForeignKey(DeviceModel, on_delete=models.CASCADE)
    color = models.ForeignKey(
        DeviceColor, on_delete=models.CASCADE, blank=True, null=True)
    carrier = models.CharField(
        max_length=25, choices=SERVICE_PROVIDER_CHOICES, default='unknown')
    imei = models.CharField(max_length=20, blank=True, null=True)
    serial_number = models.CharField(max_length=20, blank=True, null=True)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE,
                               blank=True,
                               null=True,
                               related_name='device_vendor'
                               )
    seller = models.ForeignKey(CustomUser,
                               on_delete=models.CASCADE,
                               related_name='device_seller',
                               blank=True,
                               null=True
                               )
    compatibility = models.CharField(
        max_length=25, choices=COMPATIBILITY_CHOICES, default='unknown')
    cost = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    value = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    device_created_by = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='device_created_by',
        null=True,
        blank=True
    )
    device_updated_by = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='device_updated_by',
        null=True,
        blank=True
    )
    purchase_date = models.DateField(default=datetime.now)
    device_created_date = models.DateTimeField(auto_now_add=True)
    device_updated_date = models.DateTimeField(auto_now_add=True,)
    info = models.TextField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    report = models.FileField(
        upload_to='static/reports/device_reports/',
        null=True,
        blank=True
    )
    device_defects = models.ManyToManyField(
        DeviceDefect,
        related_name='device_defects',
        help_text='Select all that apply',
        default=None
    )
    photo = models.ImageField(
        upload_to='static/images/device_photos/', null=True, blank=True)
    status = models.CharField(
        max_length=25, choices=DEVICE_CONDITION_CHOICES, default='unknown')
    grade = models.CharField(
        max_length=25, choices=DEVICE_GRADE_CHOICES, default='unknown')

    def __str__(self):
        return (self.color.name
                + ' '
                + self.device_model.brand.manufacturer.name
                + ' '
                + self.device_model.brand.name
                + ' '
                + self.device_model.name
                )

    def __repr__(self):
        return (self.color.name + ' '
                + self.device_model.brand.manufacturer.name
                + ' ' + self.device_model.brand.name
                + ' ' + self.device_model.name
                )

    class Meta:
        ordering = ('id',)
        verbose_name = 'Device'
        verbose_name_plural = 'Devices'
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////


class WorkOrder(models.Model):

    TAX_RATE = 0.09

    order_status_choices = (
        ('Pending', 'pending'),
        ('In Progress', 'in progress'),
        ('Completed', 'completed'),
        ('آخر', 'آخر'),
    )
    customer = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE,
        related_name='work_order_Customer')
    employee = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE,
        related_name='work_order_employee')
    # device = models.ForeignKey(
    #     Device, on_delete=models.CASCADE, related_name='work_order_device')
    work_order_status = models.CharField(
        max_length=25, choices=WORK_ORDER_STATUS_CHOICES, default='pending')
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    discount = models.DecimalField(
        max_digits=10, decimal_places=2, default=0.00)
    order_created_by = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='work_order_created_by',
        null=True,
        blank=True
    )
    order_updated_by = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='work_order_updated_by',
        null=True,
        blank=True
    )
    order_created_date = models.DateTimeField(auto_now_add=True)
    order_updated_date = models.DateTimeField(auto_now_add=True,)
    notes = models.TextField(blank=True, null=True)

    def __repr__(self):
        return '<WorkOrder object ({})>'.format(self.id)

    def __str__(self):
        return '{}'.format(self.id)

    class Meta:
        ordering = ('id',)
        verbose_name = 'Work Order'
        verbose_name_plural = 'Work Orders'

    def get_total_price(self):
        total_price = self.price * (1 - (self.discount / 100))
        total_price_with_tax = total_price * (1 + self.TAX_RATE)
        return total_price_with_tax
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////
# create a labor model


class Labor(models.Model):
    labor_name = models.CharField(max_length=200)
    labor_price = models.DecimalField(
        max_digits=10, decimal_places=2, default=0.00)
    labor_description = models.TextField(blank=True, null=True)
    labor_risk = models.CharField(
        max_length=25, choices=LABOR_RISK_CHOICES, default='low')

    def __str__(self):
        return self.labor_name

    def __repr__(self):
        return '<Labor object ({})>'.format(self.id)
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Subcategory(models.Model):
    name = models.CharField(max_length=100, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    DISCOUNT_RATE = 0.01
    name = models.CharField(max_length=500)
    description = models.CharField(max_length=300, blank=True, null=True)
    sku = models.CharField(max_length=100, unique=True)
    cost = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, null=True, blank=True)
    subcategory = models.ForeignKey(
        Subcategory, on_delete=models.CASCADE, null=True, blank=True)
    # labor = models.ForeignKey(Labor,
    #                           on_delete=models.CASCADE,
    #                           related_name='product_labor',
    #                           blank=True,
    #                           null=True
    #                           )
    price = models.DecimalField(
        max_digits=12, decimal_places=2, default=999.99)
    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
        default='1',
        related_name='department'
    )
    location = models.ForeignKey(
        Location,
        on_delete=models.CASCADE,
        default='1',
        related_name='location'
    )
    vendor = models.ForeignKey(
        Vendor, on_delete=models.CASCADE, default='1', related_name='vendor')
    manufacturer = models.ForeignKey(
        Manufacturer,
        on_delete=models.CASCADE,
        related_name='manufacturer',
        blank=True,
        null=True
    )
    onhand_quantity = models.IntegerField(default=0)
    min_stock_threshold = models.IntegerField(default=0)
    max_stock_threshold = models.IntegerField(default=0)
    tags = models.ManyToManyField(Tag, blank=True)
    is_featured = models.BooleanField(default=False)
    views_count = models.IntegerField(default=0)
    added_to_cart_count = models.IntegerField(default=0)
    sale_start = models.DateTimeField(blank=True, null=True, default=None)
    sale_end = models.DateTimeField(blank=True, null=True, default=None)
    notes = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published = models.BooleanField(default=True)
    photo = models.ImageField(
        blank=True,
        null=True,
        default=None,
        upload_to='static/images/store/products'
    )
    url = models.CharField(max_length=200, blank=True, null=True)
    product_created_by = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        default=None,
        related_name='product_created_by',
        blank=True,
        null=True
    )
    product_updated_by = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        default=None,
        related_name='product_updated_by',
        blank=True,

        null=True)
    ms_url = models.CharField(max_length=300, blank=True, null=True)

    def is_on_sale(self):
        now = timezone.now()
        if self.sale_start:
            if self.sale_end:
                return self.sale_start <= now <= self.sale_end
            return self.sale_start <= now
        return False

    def get_rounded_price(self):
        return round(self.price, 2)

    def current_price(self):
        if self.is_on_sale():
            discounted_price = self.price * (1 - self.DISCOUNT_RATE)
            return round(discounted_price, 2)
        return self.get_rounded_price()

    def get_margin(self):
        if self.cost:
            margin = self.price - self.cost
            return round(margin, 2)
        return 0

    def get_markup(self):
        if self.cost:
            markup = (self.price / self.cost) * 100
            return round(markup, 2)
        return 0

    def __repr__(self):
        return '<Product object ({})>'.format(self.name)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('id',)
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////


class ShoppingCart(models.Model):

    TAX_RATE = 0.09

    customer = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        default=1,
        related_name='shopping_cart_customer'
    )
    cashier = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        default=1,
        related_name='shopping_cart_cashier'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    subtotal = models.DecimalField(
        max_digits=12, decimal_places=2, default=0.00)
    total = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    discount = models.IntegerField(default=0)
    status = models.CharField(max_length=100, blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    shopping_cart_created_by = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='shopping_cart_created_by',
        null=True,
        blank=True
    )
    shopping_cart_updated_by = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='shopping_cart_updated_by',
        null=True,
        blank=True)
    ordered = models.BooleanField(default=False)

    def __repr__(self):
        return str(self.id)

    def __str__(self):
        return str(self.id)

    @property
    def tax(self):
        return round(self.subtotal * self.TAX_RATE, 2)

    @property
    def total(self):
        return round((self.subtotal + self.tax) * (1 - self.discount / 100), 2)

    def update_subtotal(self):
        self.subtotal = sum(item.product.current_price() *
                            item.quantity for item in self.cart_items.all())
        self.save()

    class Meta:
        ordering = ('id',)
        verbose_name = 'Shopping Cart'
        verbose_name_plural = 'Shopping Carts'
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////


class CartItem(models.Model):
    shopping_cart = models.ForeignKey(
        ShoppingCart, on_delete=models.CASCADE, related_name='cart_items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(
        default=1, validators=[MinValueValidator(1)])

    def __str__(self):
        return f'{self.product.name} ({self.quantity})'

    # Add a property to get the price
    # for this cart item (product price * quantity)
    @property
    def item_total(self):
        return self.product.current_price() * self.quantity
