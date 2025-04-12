document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('registrationForm');
    const phoneInput = document.getElementById('phone');
    const countryCode = document.getElementById('countryCode');

    // Форматирование номера в реальном времени
    phoneInput.addEventListener('input', function(e) {
        let x = e.target.value.replace(/\D/g, '');
        const code = countryCode.value;
        
        // Форматирование для РФ (+7)
        if (code === '7') {
            if (x.length > 0) x = x.slice(0, 10); // Ограничение 10 цифр
            if (x.length > 0) x = x.replace(/^(\d{3})(\d{3})(\d{2})(\d{2})$/, '($1) $2-$3-$4');
            phoneInput.placeholder = '(999) 999-99-99';
        } 
        // Форматирование для РБ (+375)
        else if (code === '375') {
            if (x.length > 0) x = x.slice(0, 9); // Ограничение 9 цифр
            if (x.length > 2) x = x.replace(/^(\d{2})(\d{3})(\d{2})(\d{2})$/, '$1 $2-$3-$4');
            phoneInput.placeholder = '29 999-99-99';
        }
        
        e.target.value = x;
    });

    // При изменении кода страны
    countryCode.addEventListener('change', function() {
        phoneInput.value = '';
        phoneInput.dispatchEvent(new Event('input'));
    });

    // Сохранение в JSON
    form.addEventListener('submit', function(e) {
        e.preventDefault();
        
        let formattedPhone;
        const cleanPhone = phoneInput.value.replace(/\D/g, '');
        
        if (countryCode.value === '7') {
            formattedPhone = `+7 ${phoneInput.value}`;
        } else {
            formattedPhone = `+375 ${phoneInput.value}`;
        }

        const formData = {
            name: form.name.value,
            phone: formattedPhone,
            country: countryCode.value === '7' ? 'РФ' : 'РБ',
            timestamp: new Date().toLocaleString()
        };

        // Создаем и скачиваем JSON
        const dataStr = JSON.stringify(formData, null, 2);
        const dataUri = 'data:application/json;charset=utf-8,'+ encodeURIComponent(dataStr);
        
        const exportName = `registration_${formData.country}_${new Date().getTime()}.json`;
        const linkElement = document.createElement('a');
        linkElement.setAttribute('href', dataUri);
        linkElement.setAttribute('download', exportName);
        linkElement.click();
        
        alert(`Данные сохранены!\nФайл: ${exportName}`);
        form.reset();
    });
});