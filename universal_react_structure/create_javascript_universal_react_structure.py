# create_universal_react_structure.py

import os

def create_folder(path):
    if not os.path.exists(path):
        os.makedirs(path)

def create_file_with_comment(path, comment):
    if path.endswith((".js", ".html", ".css")):
        with open(path, 'w', encoding='utf-8') as file:
            file.write(comment)

def create_empty_file(path):
    with open(path, 'wb') as file:
        pass

def create_project_structure():
    base_path = "D:/projects/universal_react_structure/"
    base_dir = os.path.join(base_path, "universal_react_structure/src/")
    create_folder(os.path.join(base_dir, "assets/images"))
    create_empty_file(os.path.join(base_dir, "assets/images/avatar.jpg"))
    create_empty_file(os.path.join(base_dir, "assets/images/logo.png"))
    create_empty_file(os.path.join(base_dir, "assets/images/background.jpg"))
    create_folder(os.path.join(base_dir, "assets/icons"))
    create_empty_file(os.path.join(base_dir, "assets/icons/facebook.svg"))
    create_empty_file(os.path.join(base_dir, "assets/icons/twitter.svg"))
    create_empty_file(os.path.join(base_dir, "assets/icons/instagram.svg"))
    # ... продолжение для остальных файлов и папок
    create_folder(base_dir + "components/Auth")
    create_file_with_comment(base_dir + "components/Auth/AuthProvider.js", "// Контекст аутентификации пользователя.")
    create_file_with_comment(base_dir + "components/Auth/Login.js", "// Компонент для входа пользователя.")
    create_file_with_comment(base_dir + "components/Auth/Register.js", "// Компонент для регистрации пользователя.")
    create_file_with_comment(base_dir + "components/Auth/SocialLogin.js", "// Компонент для входа через социальные сети.")
    # ... продолжение для остальных файлов и папок
    # ... продолжение функции create_project_structure
    create_folder(base_dir + "components/UserProfile")
    create_file_with_comment(base_dir + "components/UserProfile/UserProfile.js", "// Основной компонент профиля пользователя.")
    create_file_with_comment(base_dir + "components/UserProfile/Avatar.js", "// Компонент для отображения аватара пользователя.")
    create_file_with_comment(base_dir + "components/UserProfile/Bio.js", "// Компонент для отображения биографической информации.")

    create_folder(base_dir + "components/Settings")
    create_file_with_comment(base_dir + "components/Settings/Settings.js", "// Компонент настроек пользователя.")
    create_file_with_comment(base_dir + "components/Settings/Notifications.js", "// Компонент для управления уведомлениями.")
    create_file_with_comment(base_dir + "components/Settings/InterfaceSettings.js", "// Компонент настроек интерфейса.")

    create_folder(base_dir + "components/Messaging")
    create_file_with_comment(base_dir + "components/Messaging/Messages.js", "// Основной компонент для просмотра сообщений.")
    create_file_with_comment(base_dir + "components/Messaging/Chat.js", "// Компонент для чата.")
    create_file_with_comment(base_dir + "components/Messaging/MessageInput.js", "// Компонент для ввода сообщений.")
    create_file_with_comment(base_dir + "components/Messaging/ConversationList.js", "// Компонент для списка бесед.")

    create_folder(base_dir + "components/AdminPanel")
    create_file_with_comment(base_dir + "components/AdminPanel/AdminDashboard.js", "// Основной компонент панели администратора.")
    create_file_with_comment(base_dir + "components/AdminPanel/UserManagement.js", "// Компонент для управления пользователями.")
    create_file_with_comment(base_dir + "components/AdminPanel/ContentManagement.js", "// Компонент для управления контентом.")

    create_folder(base_dir + "components/Shared")
    create_file_with_comment(base_dir + "components/Shared/Button.js", "// Общий компонент кнопки.")
    create_file_with_comment(base_dir + "components/Shared/Input.js", "// Общий компонент ввода.")
    create_file_with_comment(base_dir + "components/Shared/Dropdown.js", "// Общий компонент выпадающего списка.")
    # ... и так далее для всех остальных папок и файлов
    # ... продолжение функции create_project_structure

    create_folder(base_dir + "contexts")
    create_file_with_comment(base_dir + "contexts/AuthContext.js", "// Контекст аутентификации.")

    create_folder(base_dir + "hooks")
    create_file_with_comment(base_dir + "hooks/useAuth.js", "// Кастомный хук для работы с аутентификацией.")
    create_file_with_comment(base_dir + "hooks/useApi.js", "// Кастомный хук для работы с API.")

    create_folder(base_dir + "services")
    create_file_with_comment(base_dir + "services/api.js", "// Сервис для обращения к API.")
    create_file_with_comment(base_dir + "services/auth.js", "// Сервис для работы с аутентификацией.")

    create_folder(base_dir + "styles")
    create_file_with_comment(base_dir + "styles/GlobalStyles.js", "// Глобальные стили.")
    create_folder(base_dir + "styles/componentStyles")
    create_file_with_comment(base_dir + "styles/componentStyles/AuthStyles.js", "// Стили для компонентов аутентификации.")
    # Добавьте остальные файлы стилей сюда

    create_folder(base_dir + "utils")
    create_file_with_comment(base_dir + "utils/helpers.js", "// Вспомогательные функции.")
    create_file_with_comment(base_dir + "utils/formatDate.js", "// Функция для форматирования дат.")
    create_file_with_comment(base_dir + "utils/validation.js", "// Функции для валидации данных.")

    create_folder(base_dir + "routes")
    create_file_with_comment(base_dir + "routes/PrivateRoute.js", "// Приватный маршрут для авторизованных пользователей.")
    create_file_with_comment(base_dir + "routes/PublicRoute.js", "// Публичный маршрут для всех пользователей.")

    create_folder(base_dir + "config")
    create_file_with_comment(base_dir + "config/config.js", "// Конфигурационные параметры приложения.")

    create_folder(base_dir + "tests")
    create_file_with_comment(base_dir + "tests/Auth.test.js", "// Тесты для компонентов аутентификации.")
    # Добавьте остальные файлы тестов сюда

    create_file_with_comment(base_dir + "App.js", "// Основной компонент приложения, определяет маршрутизацию.")
    create_file_with_comment(base_dir + "index.js", "// Точка входа в приложение.")

    create_folder("my-app/public")
    create_file_with_comment("my-app/public/index.html", "// Главный HTML файл.")

    print("Структура проекта успешно создана!")

if __name__ == "__main__":
    create_project_structure()