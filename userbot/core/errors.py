class Errors:
    """
    ## Errors
    ### Arguments:
        None
    """

    class SpamFailed(Exception):
        """
        Raises when the spam task was failed
        """

    class DownloadFailed(Exception):
        """
        Raises when the download task was failed
        """

    class DelAllFailed(Exception):
        """
        Raises when the del all function was failed
        """
