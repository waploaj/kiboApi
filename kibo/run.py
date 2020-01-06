from kibo import app,mail_handler

if not app.debug:
    app.logger.addHandler(mail_handler)

if __name__ == "__main__":
    app.run(debug=True)
