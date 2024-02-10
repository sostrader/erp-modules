from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    """
    Configure the access credentials and endpoint URL for Amazon S3 or compatible services
    """

    _inherit = "res.config.settings"

    amazon_access_key = fields.Char(
        string="Amazon S3 Access Key",
        copy=False,
        config_parameter="amazon_s3_connector.amazon_access_key",
        help="Enter your Amazon S3 Access Key here.",
    )

    amazon_secret_key = fields.Char(
        string="Amazon S3 Secret key",
        config_parameter="amazon_s3_connector.amazon_secret_key",
        help="Enter your Amazon S3 Secret Key here.",
    )

    amazon_bucket_name = fields.Char(
        string="Folder ID",
        config_parameter="amazon_s3_connector.amazon_bucket_name",
        help="Enter the name of your Amazon S3 Bucket here.",
    )

    is_amazon_connector = fields.Boolean(
        config_parameter="amazon_s3_connector.amazon_connector",
        default=False,
        help="Enable or disable the Amazon S3 connector.",
    )

    # Adiciona uma nova configuração para o host customizado
    amazon_custom_host = fields.Char(
        string="Custom S3 Host",
        config_parameter="amazon_s3_connector.custom_host",
        help="Enter your custom S3 Host URL here if you are not using Amazon S3.",
    )
